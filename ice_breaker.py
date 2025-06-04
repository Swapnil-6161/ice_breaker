from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

information="""
Elon Reeve Musk (/ˈiːlɒn/ EE-lon; born June 28, 1971) is a businessman known for his leadership of Tesla, SpaceX, X (formerly Twitter) and DOGE. Musk has been considered the wealthiest person in the world since 2021; as of May 2025, Forbes estimates his net worth to be US$424.7 billion.

Born to a wealthy family in Pretoria, South Africa, Musk emigrated in 1989 to Canada. He received bachelor's degrees from the University of Pennsylvania in 1997 before moving to California, United States, to pursue business ventures. In 1995, Musk co-founded the software company Zip2. Following its sale in 1999, he co-founded X.com, an online payment company that later merged to form PayPal, which was acquired by eBay in 2002. That year, Musk also became a U.S. citizen.

In 2002, Musk founded the space technology company SpaceX, becoming its CEO and chief engineer; the company has since led innovations in reusable rockets and commercial spaceflight. Musk joined the automaker Tesla as an early investor in 2004 and became its CEO and product architect in 2008; it has since become a leader in electric vehicles. In 2015, he co-founded OpenAI to advance artificial intelligence research but later left; growing discontent with the organization's direction in the 2020s led him to establish xAI. In 2022, he acquired the social network Twitter, implementing significant changes and rebranding it as X in 2023. In January 2025, he was appointed head of Trump's newly created DOGE. His other businesses include the neurotechnology company Neuralink, which he co-founded in 2016, and the tunneling company the Boring Company, which he founded in 2017. He was named Time magazine's Person of the Year in 2021.
"""
if __name__ == "__main__":
    print("Welcome to langchain")

    summary_template="""
     given the information {information} about a person i want you to create:
     1. a short summary
     2. two interesting facts about them
     """

    summary_prompt_template=PromptTemplate(input_variables=["information"],template=summary_template)

    llm=ChatOpenAI( model_name="gpt-3.5-turbo")

    chain=summary_prompt_template | llm

    res= chain.invoke(input={"information":information})
    print(res)
