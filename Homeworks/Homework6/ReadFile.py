import numpy as np
import astropy.units as u

def Read(filename):
    
    """
    This function will open and read any given data file according to this format,
    
        # Row 1: Time (Myr)  
        # Row 2: Total number of particles  
        # Row 3: Units for the following columns  
        # Row 4: Column headers  
        # Remaining rows contain particle data:  
        #   Col 1: Type (1=DM, 2=Disk, 3=Bulge)  
        #   Col 2: Mass (10^10 M⊙)  
        #   Col 3-5: Position (x, y, z) in kpc (MW center)  
        #   Col 6-8: Velocity (vx, vy, vz) in km/s (MW frame)  
        # Columns are tab-delimited  

    Inputs: filename (string) Name of the file in which the data is stored in the correct format.

    Output : time (Astropy units) is the time in Myr
             total_particles is the total number of particles
             data is the full data array
    """
    file = open(filename, 'r')
    line1 = file.readline()
    label, value = line1.split()
    time = float(value)*u.Myr

    line2 = file.readline()
    label, value = line2.split()
    total_particles = float(value)
    file.close()

    # Skips the first three lines and starts storing from the 4th line
    data = np.genfromtxt(filename,dtype=None,names=True,skip_header=3)
    

    return (time, total_particles, data)
