#!/usr/bin/env python3
import json
import sys
import asyncio

class WeatherServer:
    def __init__(self):
        self.weather_data = {
            "北京": {"temperature": "22°C", "condition": "晴天"},
            "上海": {"temperature": "25°C", "condition": "多云"},
            "深圳": {"temperature": "28°C", "condition": "小雨"},
            "广州": {"temperature": "27°C", "condition": "阴天"}
        }
    
    async def handle_request(self, request):
        method = request.get("method")
        
        if method == "initialize":
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {
                        "tools": {}
                    },
                    "serverInfo": {
                        "name": "weather-server",
                        "version": "1.0.0"
                    }
                }
            }
        
        elif method == "tools/list":
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": {
                    "tools": [{
                        "name": "get_weather",
                        "description": "获取指定城市的天气信息",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "city": {
                                    "type": "string",
                                    "description": "城市名称"
                                }
                            },
                            "required": ["city"]
                        }
                    }]
                }
            }
        
        elif method == "tools/call":
            tool_name = request["params"]["name"]
            if tool_name == "get_weather":
                city = request["params"]["arguments"]["city"]
                weather = self.weather_data.get(city, {"temperature": "未知", "condition": "数据不可用"})
                return {
                    "jsonrpc": "2.0",
                    "id": request.get("id"),
                    "result": {
                        "content": [{
                            "type": "text",
                            "text": f"{city}的天气：温度 {weather['temperature']}，天气状况：{weather['condition']}"
                        }]
                    }
                }
        
        return {"jsonrpc": "2.0", "id": request.get("id"), "error": {"code": -32601, "message": "Method not found"}}

async def main():
    server = WeatherServer()
    
    for line in sys.stdin:
        try:
            line = line.strip()
            if not line:
                continue
            
            request = json.loads(line)
            response = await server.handle_request(request)
            print(json.dumps(response, ensure_ascii=False))
            sys.stdout.flush()
            
        except json.JSONDecodeError:
            continue
        except Exception as e:
            error_response = {
                "jsonrpc": "2.0",
                "id": None,
                "error": {"code": -32603, "message": str(e)}
            }
            print(json.dumps(error_response))
            sys.stdout.flush()

if __name__ == "__main__":
    asyncio.run(main())