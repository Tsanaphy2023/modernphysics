# บทที่ 7: การเรียนรู้เสริมกำลัง (Reinforcement Learning) และการควบคุมระบบ

## วัตถุประสงค์
- เข้าใจหลักการของการเรียนรู้เสริมกำลังและการประยุกต์ใช้ในฟิสิกส์
- เรียนรู้อัลกอริทึม RL ที่สำคัญและการใช้งานในการควบคุมระบบ
- ประยุกต์ใช้ในการออกแบบการทดลองและการหาค่าเหมาะสมที่สุด

## 7.1 หลักการพื้นฐานของ Reinforcement Learning: Agent, Environment, Reward, State, Action

**Reinforcement Learning (RL)** เป็นสาขาหนึ่งของ Machine Learning ที่เกี่ยวข้องกับวิธีการที่ **Agent** (ตัวแทน) ควรจะกระทำใน **Environment** (สภาพแวดล้อม) เพื่อเพิ่ม **Reward** (รางวัล) สะสมสูงสุด Agent เรียนรู้จากการลองผิดลองถูก โดยการสังเกต **State** (สถานะ) ของ Environment, เลือก **Action** (การกระทำ), ได้รับ Reward และเปลี่ยนไปสู่ State ใหม่

**องค์ประกอบหลัก:**
- **Agent:** ผู้เรียนรู้หรือผู้ตัดสินใจ
- **Environment:** โลกที่ Agent โต้ตอบด้วย
- **State (S):** สถานการณ์ปัจจุบันของ Environment
- **Action (A):** การกระทำที่ Agent สามารถทำได้ในแต่ละ State
- **Reward (R):** สัญญาณตอบรับที่เป็นตัวเลขที่ Agent ได้รับหลังจากทำการ Action
- **Policy (π):** กลยุทธ์ที่ Agent ใช้ในการเลือก Action จาก State ที่กำหนด
- **Value Function (V/Q):** การประมาณค่าของ Reward ที่คาดว่าจะได้รับในอนาคตจาก State หรือ State-Action Pair หนึ่งๆ

**ตัวอย่าง:** การควบคุมหุ่นยนต์สำรวจดาวอังคารให้เคลื่อนที่ไปยังจุดที่ต้องการโดยหลีกเลี่ยงอุปสรรคและเก็บตัวอย่างแร่ธาตุ

## 7.2 Markov Decision Process (MDP) และ Bellman Equation

**Markov Decision Process (MDP)** เป็นกรอบทางคณิตศาสตร์สำหรับการสร้างแบบจำลองสถานการณ์ใน RL โดยมีคุณสมบัติ Markovian คือ สถานะในอนาคตขึ้นอยู่กับสถานะปัจจุบันและ Action ที่เลือกเท่านั้น ไม่ขึ้นอยู่กับประวัติก่อนหน้า

**Bellman Equation** เป็นสมการพื้นฐานใน RL ที่อธิบายความสัมพันธ์ระหว่าง Value Function ของสถานะปัจจุบันกับ Value Function ของสถานะถัดไป โดยพิจารณา Reward ที่ได้รับทันทีและ Reward ที่คาดว่าจะได้รับในอนาคต

**Bellman Expectation Equation (สำหรับ Value Function):**
$$V^{\pi}(s) = \sum_a \pi(a|s) \sum_{s', r} P(s', r|s, a) [r + \gamma V^{\pi}(s')]$$

**Bellman Optimality Equation (สำหรับ Optimal Value Function):**
$$V^*(s) = \max_a \sum_{s', r} P(s', r|s, a) [r + \gamma V^*(s')]$$

โดยที่ $\gamma$ คือ Discount Factor (0 ≤ $\gamma$ ≤ 1) ที่ลดทอนค่าของ Reward ในอนาคต

**ตัวอย่าง:** การใช้ MDP เพื่อสร้างแบบจำลองการควบคุมอุณหภูมิในเครื่องปฏิกรณ์นิวเคลียร์

## 7.3 อัลกอริทึม Value-based: Q-Learning และ Deep Q-Networks (DQN)

**Value-based Algorithms** มุ่งเน้นการประมาณค่า Value Function (เช่น Q-value) ของแต่ละ State-Action Pair และเลือก Action ที่มี Q-value สูงสุด

**Q-Learning:** เป็นอัลกอริทึม RL แบบ Off-policy ที่เรียนรู้ Q-function โดยตรงจากประสบการณ์ โดยไม่ต้องรู้แบบจำลองของ Environment

**สมการอัปเดต Q-value:**
$$Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$

โดยที่ $\alpha$ คือ Learning Rate

**Deep Q-Networks (DQN):** ขยายแนวคิดของ Q-Learning โดยใช้ Deep Neural Network เพื่อประมาณ Q-function ซึ่งมีประโยชน์มากสำหรับ Environment ที่มี State Space ขนาดใหญ่ เช่น การเล่นเกม Atari

**ตัวอย่าง:** การใช้ DQN เพื่อควบคุมการเคลื่อนที่ของยานสำรวจในสภาพแวดล้อมที่ซับซ้อน

## 7.4 อัลกอริทึม Policy-based: Policy Gradient และ Actor-Critic Methods

**Policy-based Algorithms** มุ่งเน้นการเรียนรู้ Policy โดยตรง ซึ่งเป็นฟังก์ชันที่แมป State ไปยัง Action โดยตรง โดยไม่ต้องประมาณ Value Function

**Policy Gradient:** อัลกอริทึมที่ปรับปรุง Policy โดยการไล่ตาม Gradient ของ Reward ที่คาดว่าจะได้รับ

**Actor-Critic Methods:** ผสมผสานแนวคิดของ Value-based และ Policy-based โดยมีสองส่วนหลัก:
- **Actor:** เรียนรู้ Policy (คล้าย Policy-based)
- **Critic:** เรียนรู้ Value Function เพื่อช่วยประเมิน Action ที่ Actor เลือก (คล้าย Value-based)

**ตัวอย่าง:** การใช้ Policy Gradient เพื่อควบคุมแขนกลให้หยิบจับวัตถุที่มีรูปร่างและน้ำหนักต่างกัน

## 7.5 การประยุกต์ใช้ในการควบคุมระบบควอนตัม (Quantum Control)

RL มีศักยภาพในการควบคุมระบบควอนตัมที่ซับซ้อน ซึ่งเป็นสิ่งสำคัญในการพัฒนา Quantum Computing และ Quantum Technologies

- **การควบคุมสปินของคิวบิต:** การใช้ RL เพื่อหาลำดับพัลส์เลเซอร์ที่เหมาะสมในการควบคุมสถานะของคิวบิต
- **การออกแบบพัลส์:** การหาพัลส์แม่เหล็กไฟฟ้าที่เหมาะสมที่สุดเพื่อกระตุ้นการเปลี่ยนสถานะควอนตัม

**ตัวอย่าง:** การใช้ RL เพื่อลดข้อผิดพลาดในการดำเนินการควอนตัม (Quantum Gate Error)

## 7.6 การออกแบบการทดลองอัตโนมัติ (Autonomous Experimental Design)

RL สามารถช่วยในการออกแบบและดำเนินการทดลองทางฟิสิกส์ได้อย่างอัตโนมัติ โดย Agent จะเรียนรู้ที่จะเลือกพารามิเตอร์การทดลองที่เหมาะสมที่สุดเพื่อบรรลุเป้าหมายที่กำหนด

- **การค้นหาวัสดุใหม่:** การใช้ RL เพื่อแนะนำองค์ประกอบและเงื่อนไขการสังเคราะห์วัสดุใหม่ที่มีคุณสมบัติเฉพาะ
- **การปรับแต่งเครื่องมือ:** การใช้ RL เพื่อปรับแต่งพารามิเตอร์ของเครื่องมือทดลอง เช่น กล้องจุลทรรศน์อิเล็กตรอน หรือเครื่องเร่งอนุภาค

**ตัวอย่าง:** การใช้ RL เพื่อเร่งกระบวนการค้นพบวัสดุตัวนำยิ่งยวดอุณหภูมิสูง

## 7.7 การหาค่าเหมาะสมที่สุดของพารามิเตอร์ในการจำลองทางฟิสิกส์

RL สามารถนำมาใช้เพื่อหาค่าพารามิเตอร์ที่เหมาะสมที่สุดในแบบจำลองทางฟิสิกส์ที่ซับซ้อน ซึ่งอาจมี State Space ขนาดใหญ่และฟังก์ชันวัตถุประสงค์ที่ซับซ้อน

- **การปรับแต่งแบบจำลองสภาพภูมิอากาศ:** การใช้ RL เพื่อหาพารามิเตอร์ที่เหมาะสมที่สุดสำหรับแบบจำลองสภาพภูมิอากาศเพื่อการพยากรณ์ที่แม่นยำยิ่งขึ้น
- **การออกแบบโครงสร้าง:** การใช้ RL เพื่อออกแบบโครงสร้างของอุปกรณ์ทางฟิสิกส์ เช่น เสาอากาศ หรือเลนส์ เพื่อให้ได้ประสิทธิภาพสูงสุด

**ตัวอย่าง:** การใช้ RL เพื่อหาพารามิเตอร์ที่เหมาะสมที่สุดสำหรับการจำลองการชนกันของกาแล็กซี

## ตัวอย่างโค้ด: Q-Learning สำหรับการควบคุมระบบควอนตัมอย่างง่าย

```python
import numpy as np

class QuantumEnv:
    def __init__(self):
        self.state = 0  # 0: Ground state, 1: Excited state
        self.actions = [0, 1] # 0: Apply pulse A, 1: Apply pulse B
        self.num_states = 2
        self.num_actions = 2

    def step(self, action):
        reward = 0
        done = False
        if self.state == 0: # Current state is Ground state
            if action == 0: # Apply pulse A (try to excite)
                if np.random.rand() < 0.7: # 70% chance to go to excited state
                    self.state = 1
                    reward = 1 # Reward for reaching excited state
                else:
                    self.state = 0
                    reward = -0.5 # Penalty for failing to excite
            elif action == 1: # Apply pulse B (do nothing effectively)
                self.state = 0
                reward = -0.1 # Small penalty for wasted action
        elif self.state == 1: # Current state is Excited state
            if action == 0: # Apply pulse A (try to de-excite)
                if np.random.rand() < 0.8: # 80% chance to go to ground state
                    self.state = 0
                    reward = 0.5 # Reward for de-exciting
                else:
                    self.state = 1
                    reward = -0.5 # Penalty for failing to de-excite
            elif action == 1: # Apply pulse B (try to maintain excited state)
                if np.random.rand() < 0.9: # 90% chance to stay excited
                    self.state = 1
                    reward = 0.2 # Small reward for maintaining state
                else:
                    self.state = 0
                    reward = -1 # Large penalty for losing excited state
        
        # End episode after a few steps or if a goal is reached (simplified for this example)
        # For simplicity, we'll let it run for a fixed number of steps in the training loop
        return self.state, reward, done, {}

    def reset(self):
        self.state = 0 # Always start in ground state
        return self.state

# Q-Learning Algorithm
def q_learning(env, num_episodes=1000, learning_rate=0.1, discount_factor=0.99, epsilon=0.1):
    q_table = np.zeros((env.num_states, env.num_actions))

    for episode in range(num_episodes):
        state = env.reset()
        done = False
        total_reward = 0

        for t in range(100): # Max 100 steps per episode
            # Epsilon-greedy strategy
            if np.random.rand() < epsilon:
                action = np.random.choice(env.actions) # Explore
            else:
                action = np.argmax(q_table[state, :]) # Exploit

            next_state, reward, done, _ = env.step(action)
            total_reward += reward

            # Q-value update
            q_table[state, action] = q_table[state, action] + \
                                     learning_rate * (reward + discount_factor * np.max(q_table[next_state, :]) - q_table[state, action])
            state = next_state
            if done: # Not used in this simplified env, but good practice
                break
        
        if episode % 100 == 0:
            print(f"Episode {episode}: Total Reward = {total_reward:.2f}")

    return q_table

# Run Q-Learning
env = QuantumEnv()
print("Training Q-Learning agent...")
optimal_q_table = q_learning(env)
print("Training complete!")
print("Optimal Q-table:")
print(optimal_q_table)

# Test the learned policy
print("\nTesting learned policy...")
state = env.reset()
for t in range(10):
    action = np.argmax(optimal_q_table[state, :])
    next_state, reward, _, _ = env.step(action)
    print(f"Step {t+1}: State {state} -> Action {action} -> Next State {next_state}, Reward {reward:.2f}")
    state = next_state
```

## บทสรุป
บทนี้ได้นำเสนอหลักการพื้นฐานของ Reinforcement Learning (RL) รวมถึงองค์ประกอบสำคัญอย่าง Agent, Environment, Reward, State และ Action นอกจากนี้ยังได้สำรวจกรอบทางคณิตศาสตร์อย่าง Markov Decision Process (MDP) และ Bellman Equation ซึ่งเป็นรากฐานของอัลกอริทึม RL ต่างๆ อัลกอริทึม Value-based เช่น Q-Learning และ Deep Q-Networks (DQN) รวมถึงอัลกอริทึม Policy-based อย่าง Policy Gradient และ Actor-Critic Methods ได้ถูกอธิบายพร้อมตัวอย่างการประยุกต์ใช้ในฟิสิกส์ เช่น การควบคุมระบบควอนตัม การออกแบบการทดลองอัตโนมัติ และการหาค่าเหมาะสมที่สุดของพารามิเตอร์ในการจำลองทางฟิสิกส์ RL เป็นเครื่องมือที่มีประสิทธิภาพในการแก้ปัญหาการควบคุมและการตัดสินใจในสภาพแวดล้อมที่ซับซ้อน และมีบทบาทสำคัญในการขับเคลื่อนการวิจัยและพัฒนาในสาขาฟิสิกส์เชิงคณิตศาสตร์

## คำถามท้ายบท
1. อธิบายความแตกต่างระหว่าง Value-based และ Policy-based methods ใน Reinforcement Learning พร้อมยกตัวอย่างอัลกอริทึมในแต่ละประเภท
2. จงออกแบบระบบ Reinforcement Learning สำหรับการควบคุมตำแหน่งของอนุภาคในกับดักแม่เหล็กไฟฟ้า (Magnetic Trap) โดยระบุ Agent, Environment, State, Action และ Reward Function ที่เหมาะสม
3. อภิปรายข้อดีและข้อจำกัดของการใช้ Reinforcement Learning ในการออกแบบการทดลองทางฟิสิกส์อัตโนมัติ เมื่อเทียบกับวิธีการออกแบบการทดลองแบบดั้งเดิม
4. อธิบายแนวคิดของ Markov Decision Process (MDP) และ Bellman Equation ในบริบทของ Reinforcement Learning และความสำคัญของมัน
5. หากคุณต้องการใช้ Deep Q-Networks (DQN) เพื่อควบคุมหุ่นยนต์สำรวจดาวอังคาร คุณจะกำหนด State, Action และ Reward อย่างไรเพื่อเพิ่มประสิทธิภาพการสำรวจและหลีกเลี่ยงอันตราย?
