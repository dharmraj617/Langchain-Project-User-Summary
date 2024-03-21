from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from third_parties.linkedin import scrape_info_from_linkdin
from agents.linkdin_lookup_agent import lookup
from output_parsers import person_intel_parser, PersonIntel
import warnings

warnings.filterwarnings("ignore")

def langchain_app(name: str) -> PersonIntel:

    linkedin_profile_url = lookup(name="Narendra Modi")

    summary_template = """
       given the information {information} about a person I want you to create:
       1. short summary
       2. Two interesting facts about them
       \n{format_instructions}
       """

    summary_prompt_template = PromptTemplate(input_variables=["information"],
                                             template=summary_template,
                                              partial_variables={
                                                  "format_instructions":person_intel_parser.get_format_instructions()
                                             },

    )

    llm = ChatOpenAI(temperature=1, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    linkdin_data = scrape_info_from_linkdin(linkedin_profile_url=linkedin_profile_url)

    result = chain.run(information=linkdin_data)

    return person_intel_parser.parse(result)


if __name__ == '__main__':
    langchain_app(name="Narendra Modi")