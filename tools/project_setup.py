 
from core import BafLog
from prompts import ProjectSetupPrompt
from api import ProjectSetupAPI

# Optionally, import any other required modules or packages
# E.g., from api import YourAPI
# E.g., from prompts import YourPrompt

class ProjectSetup:
  def __init__(self):
     self.logger = BafLog

  def execute(self,data,arg1):
    # Process data here
    response = ProjectSetupAPI.process(data)
    print("res1 ",response)
    prompt = ProjectSetupPrompt.project_setup_prompt(response)
    return prompt


        