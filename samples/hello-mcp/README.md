# 天气查询演示项目

## 项目说明
本项目提供两种实现方式的天气查询服务：
1. **MCP 版本**: 基于 Model Context Protocol，可与 Amazon Q 集成
2. **Flask API 版本**: 基于 REST API，提供 HTTP 接口

## 功能
- 支持查询北京、上海、深圳、广州的天气信息
- 提供温度和天气状况数据

## 项目结构
```
hello-mcp/
├── mcp-version/          # MCP 协议版本
│   ├── weather_server.py # MCP 服务器实现
│   ├── mcp.json         # MCP 配置文件
│   └── requirements.txt # 依赖文件
└── flask-api-version/   # Flask API 版本
    ├── weather_api.py   # Flask API 实现
    └── requirements.txt # 依赖文件
```

## MCP 版本使用方法

### 1. 配置 Amazon Q
1. 确保已安装 Python 3.7+
2. 将 `mcp-version/mcp.json` 配置到 Amazon Q 的 MCP 设置中
3. 在对话中询问天气信息，如："北京的天气怎么样？"

### 2. 手动测试 MCP 服务器
```bash
cd mcp-version
python weather_server.py
```

然后输入以下 JSON-RPC 请求进行测试：

**初始化请求：**
```json
{"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}}
```

**获取工具列表：**
```json
{"jsonrpc": "2.0", "id": 2, "method": "tools/list", "params": {}}
```

**调用天气查询工具：**
```json
{"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "get_weather", "arguments": {"city": "北京"}}}
```

## Flask API 版本使用方法

### 1. 安装依赖
```bash
cd flask-api-version
pip install -r requirements.txt
```

### 2. 启动服务
```bash
python weather_api.py
```

### 3. API 接口

**获取支持的城市列表：**
```bash
curl http://localhost:5000/weather
```

**查询指定城市天气：**
```bash
curl http://localhost:5000/weather/北京
curl http://localhost:5000/weather/上海
curl http://localhost:5000/weather/深圳
curl http://localhost:5000/weather/广州
```

**响应示例：**
```json
{
  "city": "北京",
  "temperature": "22°C",
  "condition": "晴天"
}
```