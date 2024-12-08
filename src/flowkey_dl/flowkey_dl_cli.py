import argparse
from flowkey_dl import flowkey_dl, arange_image, save_pdf

def main():
    parser = argparse.ArgumentParser(
        description="Sheet Music downloader for flowkey")
    parser.add_argument(
        "baseurl", help="Flowkey sheet music page url or url of first image. if page url is present i.e. without cdn, then all other properties can be derived"
    )
    parser.add_argument(
        "output_path",
        nargs="?",
        help="Output path for pdf",
        default="output.pdf",
    )
    
    parser.add_argument("-t", "--title", help="Title of the flowkey song")
    parser.add_argument(
        "-a",
        "--artist",
        action="store",
        type=str,
        help="Artist of the provided title",
    )
    args = parser.parse_args()
    # args = parser.parse_args(["https://cdn.flowkey.com/rendered-sheets/rXHKwugAh7rfruoZv/a0f6e032/horizontalSheet-7d7e844f-2024-10-02T08.50.png", "/Users/hannah/OneDrive/music-scores/piano/flowkey/Silent-Night-Advanced/Silent-Night-Advanced.pdf", "-t", "Silent Night", "-a", "Franz Xaver Gruber"])
    # args = parser.parse_args(["https://app.flowkey.com/player/rXHKwugAh7rfruoZv", "/Users/hannah/OneDrive/music-scores/piano/flowkey/Silent-Night-Advanced/Silent-Night-Advanced.pdf", "-t", "Silent Night", "-a", "Franz Xaver Gruber"])
    # args = parser.parse_args(["https://cdn.flowkey.com/rendered-sheets/Rvq3eyzqhe5FgmK3J/617e6589/horizontalSheet-c8e3eafc-2024-10-02T08.50.png", "/Users/hannah/OneDrive/music-scores/piano/flowkey/Ode-to-Joy--Symphony-No.-9-Beginner/Ode-to-Joy--Symphony-No.-9-Beginner.pdf", "-t", "Ode to Joy – Symphony No. 9", "-a", "Ludwig van Beethoven"])   
    pdf_path = args.output_path  # TODO: Check if input is filepath
    artist = args.artist if args.artist is not None else ""
    title = args.title if args.title is not None else ""
    image, _, _ = flowkey_dl(args.baseurl)
    processed_image = arange_image(image, title, artist)
    save_pdf(processed_image, pdf_path)


if __name__ == "__main__":
    main()
