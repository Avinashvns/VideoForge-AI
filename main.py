from app.script import ScriptProcessor


def main():

    processor = ScriptProcessor()

    script = processor.process(
        "assets/scripts/script.txt"
    )

    print("=" * 50)
    print(script.title)
    print("=" * 50)

    for paragraph in script.paragraphs:

        print(f"\nParagraph {paragraph.id}")

        for sentence in paragraph.sentences:

            print(
                f"  [{sentence.id}] {sentence.text}"
            )


if __name__ == "__main__":
    main()