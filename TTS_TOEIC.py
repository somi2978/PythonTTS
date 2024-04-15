import pandas as pd
from gtts import gTTS

def create_tts_files_from_excel(excel_file_path, english_col='단어', korean_col='뜻'):
    """
    엑셀 파일에서 영어와 한국어 텍스트를 TTS 파일로 변환합니다.

    Parameters:
    excel_file_path (str): 엑셀 파일 경로.
    english_col (str): 영어 텍스트가 포함된 열 이름. 기본값은 '단어'.
    korean_col (str): 한국어 텍스트가 포함된 열 이름. 기본값은 '뜻'.

    Returns:
    list: 영어와 한국어 TTS 파일의 경로를 포함한 리스트.
    """
    # 엑셀 파일을 읽어옵니다.
    df = pd.read_excel(excel_file_path)
    
    # 영어와 한국어 TTS 파일을 저장할 리스트를 초기화합니다.
    tts_files = []
    
    # 각 행의 영어 및 한국어 텍스트를 TTS로 변환합니다.
    for index, row in df.iterrows():
        english_text = row.get(english_col, '')
        korean_text = row.get(korean_col, '')
        
        # 영어 텍스트를 TTS로 변환
        if english_text:
            english_tts = gTTS(text=english_text, lang='en')
            english_tts_file = f'english_{index}.mp3'
            english_tts.save(english_tts_file)
            tts_files.append(english_tts_file)
        
        # 한국어 텍스트를 TTS로 변환
        if korean_text:
            korean_tts = gTTS(text=korean_text, lang='ko')
            korean_tts_file = f'korean_{index}.mp3'
            korean_tts.save(korean_tts_file)
            tts_files.append(korean_tts_file)
    
    return tts_files

# 엑셀 파일 경로를 지정하고 함수를 호출합니다.
excel_file_path = './TOEIC 1222.xlsx'
tts_files = create_tts_files_from_excel(excel_file_path)
print(f"{len(tts_files)}개의 TTS 파일이 생성되었습니다.")
