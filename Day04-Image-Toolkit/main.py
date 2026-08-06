from PIL import Image
import os


def resize_image():
    filename = input("Enter image filename: ").strip()

    try:
        img = Image.open(f"images/{filename}")

        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))

        resized = img.resize((width, height))

        name = filename.rsplit(".", 1)[0]

        resized.save(f"output/{name}_resized.png")

        print("✅ Image resized successfully!")

    except FileNotFoundError:
        print("❌ Image not found.")



def convert_format():
    file_names = input(
        "Enter image filenames separated by ',': "
    ).strip().split(",")

    for number, image in enumerate(file_names, start=1):

        image = image.strip()

        try:
            output_format = input(
                "Convert to (png, jpg, webp): "
            ).strip().lower()

            if output_format not in ["png", "jpg", "jpeg"]:
                print("❌ Unsupported format")
                continue

            name = image.rsplit(".", 1)[0]

            img = Image.open(f"images/{image}")

            if output_format in ["jpg", "jpeg"]:
                output_format = "jpeg"
                img = img.convert("RGB")

            img.save(
                f"output/{name}.{output_format}"
            )

            print(
                f"✅ {number}. {image} converted successfully!"
            )

        except FileNotFoundError:
            print(f"❌ {image} not found.")



def rotate_image():
    filename = input("Enter image filename: ").strip()

    try:
        img = Image.open(f"images/{filename}")

        angle = int(
            input("Enter rotation angle (90,180,270): ")
        )

        rotated = img.rotate(
            angle,
            expand=True
        )

        name = filename.rsplit(".",1)[0]

        rotated.save(
            f"output/{name}_rotated.png"
        )

        print("✅ Image rotated successfully!")

    except FileNotFoundError:
        print("❌ Image not found.")



def flip_image():
    filename = input("Enter image filename: ").strip()

    try:
        img = Image.open(f"images/{filename}")

        direction = input(
            "Flip direction (horizontal/vertical): "
        ).lower()

        if direction == "horizontal":
            flipped = img.transpose(
                Image.Transpose.FLIP_LEFT_RIGHT
            )

        elif direction == "vertical":
            flipped = img.transpose(
                Image.Transpose.FLIP_TOP_BOTTOM
            )

        else:
            print("❌ Invalid direction")
            return


        name = filename.rsplit(".",1)[0]

        flipped.save(
            f"output/{name}_flipped.png"
        )

        print("✅ Image flipped successfully!")

    except FileNotFoundError:
        print("❌ Image not found.")



def grayscale_image():
    filename = input("Enter image filename: ").strip()

    try:
        img = Image.open(f"images/{filename}")

        gray = img.convert("L")

        name = filename.rsplit(".",1)[0]

        gray.save(
            f"output/{name}_grayscale.png"
        )

        print("✅ Converted to grayscale!")

    except FileNotFoundError:
        print("❌ Image not found.")



def display_menu():

    print(
        """
==============================
        IMAGE TOOLKIT
==============================

1. Resize Image
2. Convert Image Format
3. Rotate Image
4. Flip Image
5. Convert to Grayscale
6. Exit

==============================
"""
    )



def main():

    os.makedirs("output", exist_ok=True)

    while True:

        display_menu()

        choice = input(
            "Choose (1-6): "
        )

        if choice == "1":
            resize_image()

        elif choice == "2":
            convert_format()

        elif choice == "3":
            rotate_image()

        elif choice == "4":
            flip_image()

        elif choice == "5":
            grayscale_image()

        elif choice == "6":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice")



if __name__ == "__main__":
    main()