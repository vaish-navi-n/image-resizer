import cv2  # Import OpenCV library for image processing

# Define the source image file name
source = "david.png"

# Define the destination file name
destination = "newdavid.jpeg"

# Define the scale percentage for resizing the image
scale_percent = 50

# Load the image from the source file using imread
image = cv2.imread(source, cv2.IMREAD_UNCHANGED)  # cv2.IMREAD_UNCHANGED flag reads the image as is.

# Check if the image was loaded successfully
if image is None:
    # Print an error message if the image cannot be loaded
    print("Error: Could not load image.")
else:
    # Display the original image in a window titled "Original Image"
    cv2.imshow("Original Image", image)

    # Calculate the new width for resizing
    new_width = int(image.shape[1] * scale_percent / 100)

    # Calculate the new height for resizing
    new_height = int(image.shape[0] * scale_percent / 100)

    # Create a tuple for the new dimensions
    dsize = (new_width, new_height)

    # Resize the image using the calculated dimensions
    output = cv2.resize(image, dsize)

    # Save the resized image to the destination file
    cv2.imwrite(destination, output)

    # Display the resized image in a window titled "Resized Image"
    cv2.imshow("Resized Image", output)

    # Wait indefinitely for a key press
    cv2.waitKey(0)

    # Close all OpenCV windows
    cv2.destroyAllWindows()
