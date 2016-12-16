NUM_CHANNELS = 3  # RGB images
PIXEL_DEPTH = 255
NUM_LABELS = 2
TRAINING_SIZE = 100
SEED = 43212  # Set to None for random seed.
EVAL_BATCH_SIZE = 64  # 64
BATCH_SIZE = 64
NUM_EPOCHS = 10  # Will later be determined by validation.
ROTATE_IMAGES = False
RESTORE_MODEL = False  # If True, restore existing model instead of training a new one
TRAIN_PREDICTIONS = True  # If True, restore existing model instead of training a new one
TEST_PREDICTIONS = True
ENABLE_RECORDING = False
RECORDING_STEP = 1000
LEARNING_RATE = 0.001

# Convolution network architecture
CONV_ARCH = [2, 2, 4]  # The best architecture so far on validation.
# [2, 4, 4, 6] Best on test set.
# We will keep both, but mostly use [2, 2, 4] because of our limited
# computation power.

# Set image patch size in pixels
# IMG_PATCH_SIZE should be a multiple of 4
# image size should be an integer multiple of this number!
IMG_PATCH_SIZE = 16

# Border for enhanced context.
IMG_BORDER = 4  # Will be set after archi is found

IMG_TOTAL_SIZE = IMG_PATCH_SIZE + 2 * IMG_BORDER

# Validation parameters:
VALIDATION_TRAIN_PERC = 0.6
VALIDATION_VAL_PERC = 0.3
VALIDATION_TEST_PERC = 0.1

# Hyperparameters validation
COMPUTE_VALIDATION_F1_SCORE_FOR_EACH_EPOCH = False

################################################################################
################################################################################
################################################################################

PP_NUM_CHANNELS = 1  # Binary images
PP_NUM_LABELS = 2
PP_TRAINING_SIZE = 100
PP_SEED = 43212  # Set to None for random seed.
PP_EVAL_BATCH_SIZE = 128  # 64
PP_BATCH_SIZE = 64
PP_NUM_EPOCHS = 6  # Will later be determined by validation.
PP_ROTATE_IMAGES = False
PP_RESTORE_MODEL = False  # If True, restore existing model instead of training a new one
PP_TRAIN_PREDICTIONS = False  # If True, restore existing model instead of training a new one
PP_TEST_PREDICTIONS = True
PP_ENABLE_RECORDING = False
PP_RECORDING_STEP = 1000
PP_LEARNING_RATE = 0.001

# Convolution network architecture
PP_CONV_ARCH = [1]

# Set image patch size in pixels
# IMG_PATCH_SIZE should be a multiple of 4
# image size should be an integer multiple of this number!
PP_IMG_PATCH_SIZE = 2  # MUST BE EVEN

# Border for enhanced context.
PP_IMG_BORDER = 8  # MUST BE EVEN (could eventually be even ....)

PP_IMG_TOTAL_SIZE = PP_IMG_PATCH_SIZE + 2 * PP_IMG_BORDER

# Validation parameters:
PP_VALIDATION_TRAIN_PERC = 0.6
PP_VALIDATION_VAL_PERC = 0.3
PP_VALIDATION_TEST_PERC = 0.1

# Hyperparameters validation
PP_COMPUTE_VALIDATION_F1_SCORE_FOR_EACH_EPOCH = False
