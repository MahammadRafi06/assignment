import os
import streamlit as st
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
# key = os.getenv('AZURE_CONVERSATIONS_KEY')
# endpoint = os.getenv('AZURE_CONVERSATIONS_ENDPOINT')
key = "CG5khfMNSDVmmlLpCQppN5q5UOMyqn5trnUXMQmJUd9k1MZORHDkJQQJ99AKACBsN54XJ3w3AAAaACOGqWs1"
endpoint = "https://mywebapp.cognitiveservices.azure.com/"


def sample_abstractive_summarization() -> None:

    text_analytics_client = TextAnalyticsClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key),
    )
    st.title(" Text Summarization App")
    st.write("This is a simple text summarization app using Azure Text Analytics")
    text = st.text_input("Enter the text you want to summarize")
    if text:
        document = [
        text
        ]

        poller = text_analytics_client.begin_abstract_summary(document)
        abstract_summary_results = poller.result()
        for result in abstract_summary_results:
            if result.kind == "AbstractiveSummarization":
                st.write("Summaries abstracted:")
                #[print(f"{summary.text}\n") for summary in result.summaries]
                for summary in result.summaries:
                    st.write(summary.text)
            elif result.is_error is True:
                print("...Is an error with code '{}' and message '{}'".format(
                    result.error.code, result.error.message
                ))


if __name__ == "__main__":
    sample_abstractive_summarization()