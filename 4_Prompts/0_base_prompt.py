
from langchain_core.prompts import PromptTemplate


prompt_template = PromptTemplate(
    template="What are the important {skill} skills for a {role}?",
    input_variables=["role", "skill"],
)

prompt_template.save("important_skills_prompt.json")