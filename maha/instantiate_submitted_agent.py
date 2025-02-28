import submitted_agent
from submitted_agent import SubmittedAgent
import camera
from camera import CameraResolution

my_agent = SubmittedAgent()
my_agent2 = SubmittedAgent()
#my_agent = RecurrentPPOAgent('recurrent')
run_match(my_agent, my_agent2, video_path='vis.mp4', resolution=CameraResolution.LOW)
Video('vis.mp4', embed=True, width=800)