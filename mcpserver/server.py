from typing import Any
import httpx

from mcp.server.fastmcp import FastMCP


# mcp = FastMCP("weather")
#Create an MCP Server
mcp = FastMCP(
    name="weather",
    host="0.0.0.0", #only used for sse(server Send) transport 
    port=8000
)

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def get_weather_request(url:str) -> dict[str, Any] | None:
    """ make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent" : USER_AGENT,
        "Accept" : "application/geo+json"
    }
    print("get weather request called")
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()

        except Exception:
            return None
        
def format_alert(feature: dict) -> str:
    """Format an alert feature into readable string"""
    properties = feature["properties"]
    
    return f"""
        Event: {properties.get('event', 'Unknown')}
        Area: {properties.get('areaDesc', 'Unknown')}
        Severity: {properties.get('severity', 'Unknown')}
        Description: {properties.get('description', 'No description is available')}
        Instructions: {properties.get('instruction', 'No specific instruction provided')}
    """

@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alert for a US state.
        Args:
            State: Two-letter US state code (e.g CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    
    data = await get_weather_request(url)
    
    if not data:
        return "There is NO data"
    
    if "features" not in data:
        return "No alert found"
    

    if not data["features"]:
        return "No active alerts for this state"
    
    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)
    



# @mcp.resource("echo://{message}")
# def echo_resource(message:str)->str:
#     """Echo a message as resource"""
#     return f"Resource Message:{message}"

#above resource commented since testing sse transport protocol

if __name__ == "__main__":
    transport = "sse"

    if transport == "stdio":
        print("Server running on stdio transport")
        mcp.run(transport="stdio")
    elif transport=="sse":
        print ("Server running on SSE transport")
        mcp.run(transport="sse")
    else:
        raise ValueError(f"Unknown transport: {transport}")






