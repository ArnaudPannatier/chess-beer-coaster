from pathlib import Path

from chess import pgn, svg

if __name__ == "__main__":
    folder = Path("..") / "pgns"
    files = sorted(folder.glob("*.pgn"))

    save_folder = Path("..") / "svgs"

    for file in files:
        game = pgn.read_game(file.open())
        print(game)
        print(game.errors)
        print(game.board())

        print(game.board().board_fen())

        svg_file = svg.board(game.board(), colors={"square dark" : "#000000", "square light": "#ffffff"})
        savefile = save_folder / (file.stem + ".svg")
        with savefile.open("w+") as outfile:
            outfile.write(svg_file)

