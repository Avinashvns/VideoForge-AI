import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.script import ScriptProcessor


def main():

    processor = ScriptProcessor()

    script = processor.process(
        "assets/scripts/script.txt"
    )

    print("=" * 50)
    print("SCRIPT SUMMARY")
    print("=" * 50)

    print(f"Title      : {script.title}")
    print(f"Paragraphs : {script.total_paragraphs}")
    print(f"Sentences  : {script.total_sentences}")
    print(f"Words      : {script.total_words}")

    print("\n" + "=" * 50)

    for paragraph in script.paragraphs:

        print(f"\nParagraph {paragraph.id}")

        for sentence in paragraph.sentences:

            print(
                f"[{sentence.id}] "
                f"Words={sentence.word_count} | "
                f"Chars={sentence.character_count}"
            )

            print(sentence.text)

            print(
                f"Duration : "
                f"{sentence.estimated_duration:.2f} sec"
            )


if __name__ == "__main__":
    main()