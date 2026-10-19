from PIL import Image

im1 = Image.open(r"c:\Users\thana\Desktop\Private-Flashcard\images\diagrams\hw6_p01_full.png")
# Fig 1 is roughly in the middle of page 1
# Let's crop Fig 1
fig1 = im1.crop((100, 480, 1600, 1100))
fig1.save(r"c:\Users\thana\Desktop\Private-Flashcard\images\diagrams\hw6_fig1_yy_balanced.png")

# Fig 2 is on bottom of page 1 and top of page 2
im2 = Image.open(r"c:\Users\thana\Desktop\Private-Flashcard\images\diagrams\hw6_p02_full.png")
fig2 = im2.crop((100, 80, 1600, 680))
fig2.save(r"c:\Users\thana\Desktop\Private-Flashcard\images\diagrams\hw6_fig2_yy_unbalanced.png")

# Fig 3 is on bottom of page 2
fig3 = im2.crop((100, 1300, 1600, 2050))
fig3.save(r"c:\Users\thana\Desktop\Private-Flashcard\images\diagrams\hw6_fig3_yy_neutral_z.png")

print("Cropped HW6 Figs 1, 2, 3 successfully")
