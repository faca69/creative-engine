import sys
sys.path.insert(0, '.')
from tools.image_gen import generate_ugc_image
try:
    res = generate_ugc_image(
        prompt='2:3. Front angle. A young woman in her mid-20s with a minimalist ring. She is holding the Shear Sciences NanoSpray bottle precisely in the center of the frame in a cozy kitchen next to a coffee cup. Natural skin texture with visible pores, subtle grain. Amateur iPhone selfie, slightly uneven framing. The Shear Sciences bottle is immutable and dead-center. No studio lighting. Realism.',
        reference_paths=['references/assets/shear_sciences/shear_sciences_bottle.jpg'],
        aspect_ratio='2:3',
        model='nano-banana-pro'
    )
    print('\nSUCCESS_RESULT:', res)
except Exception as e:
    print('\nERROR_RESULT:', e)
