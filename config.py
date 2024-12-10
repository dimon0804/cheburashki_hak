from dotenv import load_dotenv
import os


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN') 
SQLALCHEMY_URL = os.getenv('SQLALCHEMY_URL')
DEBUG = True
TIME_ZONE = "Europe/Moscow"

LANGDICT = {
    "ru": "Russian 🇷🇺",
    "en": "English 🇬🇧",
    "sq": "Albanian 🇦🇱",
    "ar": "Arabic 🇸🇦",
    "be": "Belarusian 🇧🇾",
    "bg": "Bulgarian 🇧🇬",
    "ca": "Catalan 🇪🇸",
    "zh-CN": "Chinese Simplified 🇨🇳",
    "zh-TW": "Chinese Traditional 🇹🇼",
    "hr": "Croatian 🇭🇷",
    "cs": "Czech 🇨🇿",
    "da": "Danish 🇩🇰",
    "nl": "Dutch 🇳🇱",
    "eo": "Esperanto 🌍",
    "et": "Estonian 🇪🇪",
    "tl": "Filipino 🇵🇭",
    "fi": "Finnish 🇫🇮",
    "fr": "French 🇫🇷",
    "gl": "Galician 🇪🇸",
    "de": "German 🇩🇪",
    "el": "Greek 🇬🇷",
    "iw": "Hebrew 🇮🇱",
    "hi": "Hindi 🇮🇳",
    "hu": "Hungarian 🇭🇺",
    "is": "Icelandic 🇮🇸",
    "id": "Indonesian 🇮🇩",
    "ga": "Irish 🇮🇪",
    "it": "Italian 🇮🇹",
    "ja": "Japanese 🇯🇵",
    "ko": "Korean 🇰🇷",
    "la": "Latin 🌍",
    "lv": "Latvian 🇱🇻",
    "lt": "Lithuanian 🇱🇹",
    "mk": "Macedonian 🇲🇰",
    "ms": "Malay 🇲🇾",
    "mt": "Maltese 🇲🇹",
    "no": "Norwegian 🇳🇴",
    "fa": "Persian 🇮🇷",
    "pl": "Polish 🇵🇱",
    "pt": "Portuguese 🇵🇹",
    "ro": "Romanian 🇷🇴",
    "sr": "Serbian 🇷🇸",
    "sk": "Slovak 🇸🇰",
    "sl": "Slovenian 🇸🇮",
    "es": "Spanish 🇪🇸",
    "sw": "Swahili 🇰🇪",
    "sv": "Swedish 🇸🇪",
    "th": "Thai 🇹🇭",
    "tr": "Turkish 🇹🇷",
    "uk": "Ukrainian 🇺🇦",
    "vi": "Vietnamese 🇻🇳",
    "cy": "Welsh 🏴",
    "yi": "Yiddish 🌍",
}

LANGUES = LANGDICT.keys()
