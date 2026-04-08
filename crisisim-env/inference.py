from crisissim.env import CrisisSimEnv

env = CrisisSimEnv()

state = env.reset()
done = False

while not done:
    # Dummy agent action
    action = {"decision": "analyze"}
    state, reward, done, info = env.step(action)

print("Final state:", state)
print("Total reward:", reward)