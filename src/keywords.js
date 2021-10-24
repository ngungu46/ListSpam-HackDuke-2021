Survey
    .StylesManager
    .applyTheme("modern");

var json = {
    "pages": [
        {
            "name": "page1",
            "elements": [
                {
                    "type": "checkbox",
                    "name": "skill",
                    "isRequired": true,
                    "title": "Rank your top potential skills",
                    "colCount": 4,
                    "choicesOrder": "asc",
                    "choices": [
                        "C++",
                        "python",
                        "JavaScript",
                        "teamwork",
                        "presentation",
                        "music production",
                        "cooking",
                        "photography",
                        "hardware",
                        "PPT"
                    ]
                }, {
                    "type": "ranking",
                    "name": "bestskill",
                    "isRequired": true,
                    "visibleIf": "{skill.length} > 1",
                    "title": "What skill did you enjoy the most?",
                    "choicesFromQuestion": "skill",
                    "choicesFromQuestionMode": "selected"
                }
            ]
        }
    ]
};

window.survey = new Survey.Model(json);

survey
    .onComplete
    .add(function (sender) {
        document
            .querySelector('#surveyResult')
            .textContent = "Result JSON:\n" + JSON.stringify(sender.data, null, 3);
    });

survey.render("surveyElement");