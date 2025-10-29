import os  
from langchain_google_genai import ChatGoogleGenerativeAI # type: ignore
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate # <-- Added this import for the prompt
from tools import get_soil_npk, get_weather_info
from prompt import prompt_template

load_dotenv()

tools = [get_soil_npk, get_weather_info]

class SoilAgent:
    def __init__(self):
        self.model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=0)
        # We get the prompt from the prompt.py file
        self.prompt = PromptTemplate.from_template(prompt_template) 
        self.tools = tools

    # create a react agent
    def agent_creator(self):
        agent = create_react_agent(
            llm=self.model,
            tools=self.tools,
            prompt=self.prompt
        )
        return agent
    
    # Run the soilagent
    def run(self, location: str):
        agent = self.agent_creator()
        
        initial_message = f"""You are a soil health expert AI agent. Your task is to analyze soil health data and provide recommendations for improving soil quality.
        
        First, get the soil NPK data for the location at latitude {latitude} and longitude {longitude}.
        
        Second, gather the current weather information for the city: {location}.
        
        Finally, based on *both* the soil NPK data and the current weather conditions, provide actionable recommendations to enhance soil fertility and overall health."""

        # Instantiate AgentExecutor
        executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True
        )
        
        # Pass the input as a dictionary
        response = executor.invoke(
            {"input": initial_message}
        )
        
        return response
    
if __name__ == "__main__":
    soil_agent = SoilAgent()
    
    # <-- FIX 1: Provide all the required data for the test
    location = "Mancherial" 
    
    
    try:
        response = soil_agent.run(
            location=location, 
            
        )
        
        print("\n--- Agent Response ---")
        print(response.get('output'))
        
    except Exception as e:
        print(f"An error occurred: {e}")