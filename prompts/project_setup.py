 
from core import BafLog
# Optionally, import any other required modules or packages

class ProjectSetupPrompt:  # Replace ProjectSetup with the name of your prompt
    def project_setup_prompt(data):
        prompt = """
            Generate a Project Object like in the example below based on the user input
            
            Rules: 
            - Only Return the Object without any texts
            - Add all needed commands to install the framworks one by one
            - if the requested framworks aren't available, return 404 error object  ( Find the Exanple Below)
            
            
            Example:
            {{
            'project_name':'Project Name',
            'backend_framework':'Laravel',
            'front_end_framework':'Nuxt 3',
            'install_backend_framework_command':['first_comand_to_run','second_comand_to_run'],
            'install_front_end_framework_command':['first_comand_to_run','second_comand_to_run']
            }}
            
           
           Error Example: 
           
              {{
               'error':'The requested framework is not available',
               'status': 404
               }}
            
            
            User Input: {data}
        """
        return prompt.format(data=data)
        