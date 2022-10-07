# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
import pandas as pd
from bs4 import BeautifulSoup



def convert_qsf():
    """
    Take a qsf file from the command line and create a csv file with the question
    information in a format that can be uploaded to metricwire/catalyst.

    https://gist.github.com/ctesta01/d4255959dace01431fb90618d1e8c241
    ^super helpful
    """
    # Read QSF file into memory
    file = open('./original.qsf', 'r')
    qsf = json.loads(file.read())
    print(qsf.keys())
    file.close()

    # find the items that are actually questions
    questions = []
    for item in qsf['SurveyElements']:
        question = {}
        if item['Element'] == "SQ":
            question['label'] = item['PrimaryAttribute']
            html_str = item['Payload']['QuestionText']
            soup = BeautifulSoup(html_str, features="html.parser")
            question['text'] = soup.get_text()
            question['qualtrics_type'] = item['Payload']['QuestionType']
            if "Choices" in item['Payload'].keys():
                choice_dict = item['Payload']['Choices']
                # choices come in as a dictionary where each key contains a sub-dictionary of "Display": value_we_want
                question['choices'] = "|".join([choice['Display'] for choice in choice_dict.values()])

            if "RecodeValues" in item['Payload'].keys():
                question['recoded'] = True
                choice_dict = item['Payload']['RecodeValues']
                question['choices'] = "|".join([choice['Display'] for choice in choice_dict.values()])
            questions.append(question)
    import pdb; pdb.set_trace()
    qualtrics_types = {
        "MC": "Multiple Choice",
        "TE": "Text Entry",
        "DB": "Descriptive Box",
        "Matrix": "Matrix",
        "SBS": "Side by side",
        "DD": "Drop-down",
    }
    print(f"Found {len(questions)} Questions in QSF")


    """
    Qualtrics fields
        Survey Entry -- irrelevant here aside from survey name
        Survey Elements 
    """

    """
    Catalyst Fields
        question
            The question content.
            "How are you feeling right now?"	
        variableName
            a shorthand name for the item.
            "now_feeling"
        type
            Metricwire Question type for the item.
            Options:
                TEXT
                SINGLE_CHOICE
                SLIDING_SCALE
                RANGE_SCALE
                MULTIPLE_CHOICE
                INFORMATION
                DROPDOWN
                PHONE_NUMBER
                PERCENT
                NUMERIC
                GEOLOCATION
                EMAIL
                DATE
                TIME
                PICTURE
                AUDIO
                VIDEO
        choices
            choices to decided between for the question. Separated by "|"
            "Choice 1|Choice 2|Choice 3"	
        pipeId
            unknown	
        disabled
            is the question disabled (hidden) in the survey right now	
        private
            unknown	
        required
            is a response required for participant to proceed	
        confirmSkip	
            should a popup ask if the participant is sure before skipping
        randomize
            should the choice orderings be randomized	
        timeToAnswer
            should participants answer within a certain time limit (seconds)	
        timeToNextQuestion
            how long must participants wait until being able to proceed to the next item	
        startLabel
            left-hand label for the scale	
        endLabel
            right-hand label for the scale	
        ## The following all take a url of a file which should be embedded in the item for display    
        pictureAttachment	
        audioAttachment	
        videoAttachment	
        pdfAttachment	
        webAttachment
        attachmentText	
        lengthLimit	
            response length limit
        dynamicCondition
            leave blank	
        rows
            for matrix type question?	
        columns
            for matrix type question?	
        rangeSettingsMin
            leave blank	
        rangeSettingsStepSize
            leave blank	
        rangeSettingsChoiceSteps
            bar separated "|"	
        groups
            question groups for each item
    """

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    convert_qsf()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
