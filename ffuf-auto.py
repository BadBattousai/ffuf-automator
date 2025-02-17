import subprocess

def run_ffuf(url, wordlist):
    # Construct the ffuf command with status code filters and recursion
    output_filename = f"output_{url.replace('http://', '').replace('https://', '').replace('/', '_')}.html"
    command = [
        "ffuf",
        "-u", f"{url}/FUZZ",
        "-w", wordlist,
        "-o", output_filename,
        "-of", "html",
        "-mc", "200,300-399,500",
        "-recursion",
        "-recursion-depth", "4"
    ]

    # Run the ffuf command
    try:
        subprocess.run(command, check=True)
        print(f"[+] Completed: {url} - Output saved to {output_filename}")
    except subprocess.CalledProcessError as e:
        print(f"[!] Error running ffuf on {url}: {e}")

def main():
    # Get wordlist and URL list file paths from user input
    wordlist = input("Enter the path to the wordlist: ")
    urls_file = input("Enter the path to the URLs file: ")

    # Read URLs from the specified file
    try:
        with open(urls_file, "r") as file:
            urls = file.read().splitlines()
    except FileNotFoundError:
        print(f"[!] {urls_file} not found.")
        return

    # Run ffuf for each URL
    for url in urls:
        if url:
            print(f"[+] Running ffuf on: {url}")
            run_ffuf(url, wordlist)

if __name__ == "__main__":
    main()
