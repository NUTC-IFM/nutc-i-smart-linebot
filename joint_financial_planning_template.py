# -*- coding: utf8 -*-
""" 退休財務規劃 模板 """

base_select_module = {
    "type": "bubble",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "退休財務規劃",
                "weight": "bold",
                "size": "xl"
            }
        ],
        "alignItems": "center"
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "spacing": "md",
        "paddingStart": "md",
        "paddingEnd": "md"
    }
}


setting_module = {
    "type": "box",
    "layout": "horizontal",
    "contents": [
        {
            "type": "text",
            "text": " ",
            "flex": 4,
            "size": "md",
            "weight": "bold",
            "align": "center",
            "gravity": "center",
            "adjustMode": "shrink-to-fit"
        },
        {
            "type": "separator"
        },
        {
            "type": "text",
            "text": " ",
            "flex": 3,
            "size": "md",
            "weight": "bold",
            "align": "center",
            "gravity": "center",
            "adjustMode": "shrink-to-fit"
        },
        {
            "type": "text",
            "text": " ",
            "flex": 1,
            "size": "md",
            "weight": "bold",
            "align": "center",
            "gravity": "center",
            "adjustMode": "shrink-to-fit"
        },
        {
            "type": "filler"
        },
        {
            "type": "button",
            "adjustMode": "shrink-to-fit",
            "action": {
                "type": "postback",
                "label": "設定",
                "data": " "
            },
            "flex": 3,
            "color": "#CB8BBD",
            "style": "primary",
            "height": "sm"
        }
    ],
    "paddingAll": "sm"
}


base_question_module = {
    "type": "bubble",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "退休財務規劃",
                "weight": "bold",
                "size": "xl"
            }
        ],
        "alignItems": "center"
    },
    "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "image",
                "url": "https://i.imgur.com/dA4mZng.png",
                "align": "center",
                "size": "full",
                "gravity": "center"
            }, {
                "type": "text",
                "text": " ",
                "size": "lg",
                "wrap": True
            }
        ],
        "alignItems": "center",
        "paddingStart": "xxl",
        "paddingEnd": "xxl",
        "paddingBottom": "xxl"
    }
}

insurance_type_select_base_module = {
    "type": "bubble",
    "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "退休財務規劃",
                "weight": "bold",
                "size": "xl"
            }
        ],
        "alignItems": "center"
    },
    "hero": {
        "type": "box",
        "layout": "vertical",
        "contents": [
            {
                "type": "text",
                "text": "類型選擇",
                "gravity": "center",
                "align": "center",
                "size": "lg"
            }
        ]
    },
    "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [],
        "spacing": "md",
        "paddingStart": "md",
        "paddingEnd": "md"
    }
}

insurance_type_select_option_module = {
    "type": "button",
    "action": {
        "type": "postback",
        "label": "action 1",
        "data": "hello",
        "displayText": "world"
    },
    "color": "#CB8BBD",
    "style": "primary",
    "height": "md",
    "gravity": "center",
    "adjustMode": "shrink-to-fit"
}


totle_result_module = {
    "type": "box",
    "layout": "vertical",
    "contents": [
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "類型：",
                    "weight": "bold",
                    "gravity": "center",
                    "size": "lg",
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": " ",
                    "size": "lg",
                    "weight": "bold",
                    "wrap": True
                }
            ]
        },
        {
            "type": "separator",
            "color": "#000000",
            "margin": "md"
        },
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "建議保險項目：",
                    "weight": "bold",
                    "gravity": "center",
                    "size": "lg",
                    "flex": 1,
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": " ",
                    "size": "lg",
                    "weight": "bold",
                    "flex": 3,
                    "wrap": True
                }
            ],
            "margin": "md"
        },
        {
            "type": "separator",
            "color": "#000000",
            "margin": "md"
        },
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "保險方向：",
                    "weight": "bold",
                    "gravity": "center",
                    "size": "lg",
                    "flex": 1,
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": " ",
                    "size": "lg",
                    "weight": "bold",
                    "flex": 3,
                    "wrap": True
                }
            ],
            "margin": "md"
        },
        {
            "type": "separator",
            "color": "#000000",
            "margin": "md"
        },
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "保費：",
                    "weight": "bold",
                    "gravity": "center",
                    "size": "lg",
                    "flex": 1,
                    "wrap": True
                },
                {
                    "type": "text",
                    "text": " ",
                    "size": "lg",
                    "weight": "bold",
                    "flex": 3,
                    "wrap": True
                }
            ],
            "margin": "md"
        },
        {
            "type": "separator",
            "color": "#000000",
            "margin": "md"
        },
        {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "說明：",
                    "weight": "bold",
                    "gravity": "center",
                    "size": "lg",
                    "flex": 1,
                    "wrap": True
                }
            ],
            "margin": "md"
        }
    ],
    "spacing": "md",
    "paddingStart": "md",
    "paddingEnd": "md"
}


insurance_description_module = {
    "type": "box",
    "layout": "horizontal",
    "contents": [
        {
            "type": "text",
            "text": "保障續約的壽險主要幫助家人，如果還沒有家庭要撫養，可以先不買。",
            "weight": "bold",
            "gravity": "center",
            "size": "lg",
            "flex": 3,
            "wrap": True
        }
    ],
    "backgroundColor": "#FFFFFF"
}


quickreply = {
    "items": [
        {
            "action": {
                "label": "功能列表",
                "text": "功能列表",
                "type": "message"
            },
            "type": "action"
        },
        {
            "action": {
                "label": "適合性分析",
                "text": "適合性分析",
                "type": "message"
            },
            "type": "action"
        },
        {
            "action": {
                "label": "汽車保險規劃",
                "text": "汽車保險規劃",
                "type": "message"
            },
            "type": "action"
        },
        {
            "action": {
                "label": "人生保險規劃1",
                "text": "人生保險規劃1",
                "type": "message"
            },
            "type": "action"
        },
        {
            "action": {
                "label": "人生保險規劃2",
                "text": "人生保險規劃2",
                "type": "message"
            },
            "type": "action"
        },
        {
            "action": {
                "label": "保障缺口分析",
                "text": "保障缺口分析",
                "type": "message"
            },
            "type": "action"
        },
        {
            "action": {
                "label": "退休財務規劃",
                "text": "退休財務規劃",
                "type": "message"
            },
            "type": "action"
        }
    ]
}
