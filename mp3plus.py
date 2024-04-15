from pydub import AudioSegment

def combine_audio_files(start, end, alphabet, num_repeats):

    # 영어 MP3 파일 목록과 한국어 MP3 파일 목록을 생성합니다.
    english_files = [f"english_{i}.mp3" for i in range(start, end)]
    korean_files = [f"korean_{i}.mp3" for i in range(start, end)]
    
    # 출력 파일 경로를 지정합니다.
    output_file_path = f"combined_audio_2t_{alphabet}.mp3"
    
    # 병합할 빈 AudioSegment 객체를 생성합니다.
    combined_audio = AudioSegment.empty()
    
    # 영어 파일과 한국어 파일을 번갈아 가며 병합합니다.
    for eng_file, kor_file in zip(english_files, korean_files):
        # 영어 MP3 파일을 로드합니다.
        english_audio = AudioSegment.from_file(eng_file)
        # 한국어 MP3 파일을 로드합니다.
        korean_audio = AudioSegment.from_file(kor_file)
        
        # 영어와 한국어 오디오를 num_repeats 횟수만큼 반복하여 병합합니다.
        for _ in range(num_repeats):
            combined_audio += english_audio
            combined_audio += korean_audio
    
    # 병합된 오디오를 MP3 파일로 저장합니다.
    combined_audio.export(output_file_path, format="mp3")
    
    print(f"영어와 한국어 MP3 파일을 번갈아 가며 병합하여 {output_file_path}에 저장했습니다.")

# 영어 MP3 파일과 한국어 MP3 파일을 번갈아 가며 병합하고, 병합된 오디오를 MP3 파일로 저장합니다.
combine_audio_files(0, 177, "AB", 2)
combine_audio_files(177, 338, "C", 2)
combine_audio_files(338, 444, "D", 2)
combine_audio_files(444, 545, "E", 2)
combine_audio_files(545, 613, "FGH", 2)
combine_audio_files(613, 707, "I", 2)
combine_audio_files(707, 792, "JKLMN", 2)
combine_audio_files(792, 934, "OP", 2)
combine_audio_files(934, 1049, "QR", 2)
combine_audio_files(1049, 1221, "STUVWXYZ", 2)
