import argparse
import openai

if __name__ == "__main__":

    prog = argparse.ArgumentParser()
    prog.add_argument("--assistant", help="Notes Assistant", required=True, action="store", dest="assistant")
    prog.add_argument("--file", help="File to process", required=True, action="store", dest="file")
    prog.add_argument("--output", help="Output file", required=False, action="store", dest="output")
    args = prog.parse_args()

    with(open(args.file, "r")) as f:
        content = f.read()

        if args.assistant == "quarterly_summary":

            with(open("./prompts/quarterly_summary.txt", "r")) as f:
                prompt_template = f.read()
                chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt_template.format(completed_tasks=content)}])
                print(chat_completion.choices[0].message.content, file=open(args.output, "w"), flush=True)