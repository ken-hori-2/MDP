class algorithm():

    def __init__(self, s, stressfull):
        self.s = s
        self.max = stressfull
        self.trigar = False
        self.select = False
        self.bp = False
        self.down = False
        self.branch = False
        self.save = False
        self.BPLIST = []
        # self.NODELIST = [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.NODELIST = [1, 1, 0, 0, 0, 0, 0]
        self.NODELIST = [1, 1, 1, 0, 0, 0, 0]

        self.NODELIST = [1, 1, 0, 1, 0, 0, 0]
        
        # self.NODELIST = [1, 1, 1, 1, 0, 0, 0]
        # self.NODELIST = [1, 1, 0, 0, 1, 0, 0]
        # self.NODELIST = [1, 1, 0, 0, 1, 1, 0]
        # self.NODELIST = [1, 0, 1, 0, 1, 1, 0]

        # self.NODELIST = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        # self.NODELIST = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0]

        
        self.next_bp = 0
        print("NODE LIST :{}".format(self.NODELIST))
    
    def model(self, a, done, i, j):
        
        
        if self.s < self.max:
            print("stress:{}".format(self.s))
            if self.NODELIST[i] == 1 and not self.save: # and self.NODELIST[count+1] == 0:
                print("Node発見")
                self.BPLIST.append(i)
                # 一個前が1ならpopで削除
                print("削除前 {}".format(self.BPLIST))
                
                if self.NODELIST[i - 1] == 1: #  and i != 1:
                    self.BPLIST.pop(-2)
                    print("削除後 {}".format(self.BPLIST))
                
                print("storage  BPLIST:{}".format(self.BPLIST))
                self.save = True
                # statemachine.save_BP(None)
                return done, i ,j

            if self.save:
                self.save = False
                # statemachine.RE_UP(None)
                # return done, i



            i += 1
            print("################")
            # print("===============")
            # statemachine.UP(None)
            
            if self.NODELIST[i] == 0: 
                print("Node未発見")   
                self.s += a
                
            return done, i ,j
        

        if self.s >= self.max and not self.trigar:
            self.trigar = True
            self.select = True
            print("stressfull")
            # statemachine.add_stress(None)
            return done, i ,j
        

        if self.select:
            self.select = False
            self.bp = True
            print("bp")
            print("next bp:{}".format(self.next_bp))
            # self.next_bp = self.BPLIST[-1]  # 優先度で後ろから順に戻る -1 -> -j
            try:
                self.next_bp = self.BPLIST[-j]
                print("[next bp : NODE {}]".format(self.next_bp))
            except:
                print("これ以上戻れません 終了します")
                # add 0724
                # done = True  # ループさせない時はこれを戻す 以下は最初の状態に戻す為に必要 # コメントアウト0725
                i = self.next_bp # 0 # コメントアウト0725
                j = 1
                self.bp = False
                self.s = 0
                self.trigar = False
                self.BPLIST.clear() # コメントアウト0725
                print("i, j = {},{} BP list:{}".format(i, j, self.BPLIST))
            # print("[next bp : NODE {}]".format(self.next_bp))
            # statemachine.select_BP(None)
            return done, i, j
        

        if self.bp:
            self.bp = False
            self.down  = True
            print("down")
            a = True
            while a:
                i -= 1
                # print("################")
                print("-----------")
                print("[NODE {}]".format(i))
                if i == self.next_bp:
                    a = False
            print("-----------")
            # statemachine.DOWN(None)
            return done, i, j
        

        if self.down:
            self.down = False
            # self.branch = True  コメントアウト 0724




            print("afterdown decision")
            # statemachine.after_DOWN(None)

            # add
            self.select = True
            j += 1
            return done, i, j
        

        # if self.branch: # コメントアウト 0724
        #     self.branch = False
        #     print("branch")
        #     done = True
        #     # statemachine.BRANCH(None)
        #     return done, i, j



# add


if __name__ == "__main__":
    done = False
    s = 0
    stressfull = 3 # 5
    a = 1
    # filename = '/Users/ken/Desktop/stress simulation/MDP/Stress_simulation/practice/statemachine/animation/fig_main/'

    algo = algorithm(s, stressfull)
    
    count = 0
    i = 0
    j = 1

    state_history = []
    while not done:
        # print("################")
        # print("===============")
        print("{} NODE {}".format(count, i))
        state_history.append(i)
        
        done , i , j = algo.model(a, done, i, j)

        print("⇩")

        count += 1


        # add 0724
        if count > 100:
            done = True
            break

    print("state history : {}".format(state_history))