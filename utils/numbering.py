# FDI tooth numbering system
def assign_fdi_numbers(teeth_boxes):

    teeth_boxes = sorted(teeth_boxes,key=lambda x:x[0])

    numbers=[]

    for i,box in enumerate(teeth_boxes):

        numbers.append(i+1)

    return numbers
