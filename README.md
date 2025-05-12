# PE05 - Image Manipulation in Python

---

## Objective
This exercise focuses on enhancing an input image using basic image manipulation techniques available in Python's `PIL` (Pillow) library.  
The purpose is to improve the clarity, brightness, sharpness, and contrast of the image to make important elements (such as people, trees, and building details) more visible and easier to identify.

## Used Libraries
- **PIL (Pillow)**: For image manipulation (`Image`, `ImageEnhance`, `ImageFilter`)
- **Matplotlib**: For displaying the image (`matplotlib.pyplot`)

## Tasks Performed
1. Loaded the provided input image (`PE05-input.jpg`) and converted it to RGB format.
2. Applied the following enhancements:
    - **Brightness Increase (1.5x)**: Slightly increased the overall brightness to make the image lighter while avoiding overexposure.
    - **Contrast Increase (1.2x)**: Enhanced the contrast moderately to better separate the dark and bright areas.
    - **Detail Enhancement (DETAIL filter)**: Applied detail filter to bring out fine textures.
    - **Sharpness Increase (1.5x)**: Made the objects and edges more defined and visible.
    - **Smooth More Filter**: Applied a smoothing filter to reduce minor noise and make the image cleaner.
3. Displayed the enhanced image using `matplotlib`.
4. Saved the final result as `PE05-output.jpg`.
5. Answered the observation questions in the code comments.

## Output Image
The enhanced image was saved as `PE05-output.jpg`.  
This version has clearer visibility of the subjects and objects in the scene, while preserving a natural appearance without over-enhancement.

## Questions and Detailed Answers

1. **How many people do you see in the output image?**  
   - Answer: There are two people clearly visible walking on the sidewalk.  
     They appear on the left side of the image, with one person slightly ahead of the other.

2. **How many trees can you identify?**  
   - Answer: Two trees are visible after enhancement.  
     One is positioned along the sidewalk near the walking people, and another can be seen further behind it.

3. **How many windows can you identify on the 2nd floor of the first building (labelled as "1") on the right-hand side of the road?**  
   - Answer: Three windows can be observed on the second floor of the first building labeled as "1" on the right side of the road.

4. **How many windows can you identify in the second building (labeled as "2") on the right-hand side of the road facing you?**  
   - Answer: Six windows are visible on the facade of the building labeled as "2", which faces directly toward the viewer on the right side.