def detect_missing_teeth(teeth_boxes):

    if len(teeth_boxes)<32:

        missing = 32-len(teeth_boxes)

    else:

        missing = 0

    return missing
