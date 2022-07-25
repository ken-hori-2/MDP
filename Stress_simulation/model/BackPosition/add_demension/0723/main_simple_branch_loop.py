# main_simple_branch copy 2.py のループ ver.
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
        self.BPLIST_2 = []

        self.NODELIST = [1, 1, 0, 0, 0, 0, 0]
        # self.NODELIST = [1, 1, 1, 0, 0, 0, 0]

        # self.NODELIST = [1, 1, 0, 1, 0, 0, 0]

        self.NODELIST_2 = [0, 0, 0, 0, 0, 0, 0]
        
        # self.NODELIST = [1, 1, 1, 1, 0, 0, 0]
        # self.NODELIST = [1, 1, 0, 0, 1, 0, 0]
        # self.NODELIST = [1, 1, 0, 0, 1, 1, 0]
        # self.NODELIST = [1, 0, 1, 0, 1, 1, 0]

        # self.NODELIST = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
        # self.NODELIST = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0]

        
        self.next_bp = 0

        self.branch_type = 0
        self.first = True
        print("NODE LIST :{}".format(self.NODELIST))
    
    def model(self, a, done, i, j, branch_type):
        
        
        
        if self.s < self.max:
            if branch_type == 0:
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
                    return done, i ,j, branch_type

                if self.save:
                    self.save = False

                i += 1
                print("################")
                
                if self.NODELIST[i] == 0: 
                    print("Node未発見")   
                    self.s += a
                    
                return done, i ,j, branch_type


            elif branch_type == 1:
                print("-  stress:{}".format(self.s))
                if self.NODELIST_2[-i] == 1 and not self.save: # and self.NODELIST[count+1] == 0:
                    print("-  Node発見")
                    
                    self.save = True
                    # statemachine.save_BP(None)
                    return done, i ,j, branch_type
                
                else:
                    if self.first:
                        self.BPLIST_2.append(1)
                    self.first = False

                if self.save:
                    self.save = False

                    ######################
                    self.BPLIST_2.append(i)
                    # 一個前が1ならpopで削除
                    print("-  削除前 {}".format(self.BPLIST_2))
                    
                    if self.NODELIST_2[-i - 1] == 1: #  and i != 1:
                        self.BPLIST_2.pop(-2)
                        print("-  削除後 {}".format(self.BPLIST_2))
                    
                    print("-  storage  BPLIST:{}".format(self.BPLIST_2))
                    ######################
                    

                i += 1
                print("################")
                # statemachine.UP(None)
                
                if self.NODELIST_2[i] == 0: 
                    # self.BPLIST_2.append(i)
                    print("Node未発見")   
                    print("-  storage  BPLIST:{}".format(self.BPLIST_2))
                    self.s += a
                    
                return done, i ,j, branch_type
        
        if self.s >= self.max and not self.trigar:
            self.trigar = True
            self.select = True
            print("stressfull")
            print("-  stress:{}".format(self.s))
            # statemachine.add_stress(None)
            return done, i ,j, branch_type

        
        # add 0724
        if self.branch: # コメントアウト 0724
            self.branch = False
            print("##################\nbranch\n##################")
            # done = True
            branch_type += 1
            j = 1
            self.bp = False
            self.s = 1 # 0
            self.trigar = False
            # self.BPLIST.clear()
            print("type:{}".format(branch_type))
            return done, i, j, branch_type
    
        if self.select:
            if branch_type == 0:
                self.select = False
                self.bp = True
                print("bp")
                # self.next_bp = self.BPLIST[-1]  # 優先度で後ろから順に戻る -1 -> -j
                try:
                    self.next_bp = self.BPLIST[-j]
                    print("[next bp : NODE {}]".format(self.next_bp))
                except:
                    print("これ以上戻れません 終了します")
                    # add 0724
                    # done = True  # ループさせない時はこれを戻す 以下は最初の状態に戻す為に必要

                return done, i, j, branch_type
            elif branch_type == 1:
                self.select = False
                self.bp = True
                print("bp")
                # self.next_bp = self.BPLIST[-1]  # 優先度で後ろから順に戻る -1 -> -j
                try:
                    self.next_bp = self.BPLIST_2[-j]
                    print("[next bp : NODE {}]".format(self.next_bp))
                except:
                    print("これ以上戻れません 終了します")
                    # add 0724
                    # done = True  # ループさせない時はこれを戻す 以下は最初の状態に戻す為に必要

                return done, i, j, branch_type
                    
            else: # loop

                # done = True  # ループさせない時はこれを戻す 以下は最初の状態に戻す為に必要

                self.select = False
                #####
                i = 1
                j = 1
                self.bp = False
                self.s = 0
                self.trigar = False
                self.BPLIST.clear()
                print("i, j = {},{} BP list:{}".format(i, j, self.BPLIST))
                branch_type = 0
                self.BPLIST.append(1) # Node 1までは進んでいるから
                print("type:{}".format(branch_type))
                #####

                return done, i, j, branch_type
                
        if self.bp:
            if branch_type == 0:
                self.bp = False
                self.down  = True
                print("down")
                a = True
                while a:
                    i -= 1
                    print("-----------")
                    print("[NODE {}]".format(i))
                    if i == self.next_bp:
                        a = False
                print("-----------")
                return done, i, j, branch_type

            elif branch_type == 1:
                self.bp = False
                self.down  = True
                print("down")
                a = True
                while a:
                    i -= 1
                    print("-----------")
                    print("[NODE {}]".format(-i))
                    if i == -self.next_bp:
                        a = False
                print("-----------")
                return done, i, j, branch_type
        

        if self.down:
            self.down = False
            self.branch = True  # コメントアウト 0724

            print("afterdown decision")

            # add
            self.select = True
            j += 1
            return done, i, j, branch_type


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
    branch_type = 0

    state_history = []
    while not done:
        
        done , i , j, branch_type = algo.model(a, done, i, j, branch_type)

        if branch_type == 0:
            print("{} NODE {}".format(count, i))
            state_history.append(i)
        elif branch_type == 1:
            print("{} NODE {}".format(count, -i))
            state_history.append(-i)
        # else:
        #     # state_history.append(i)
        #     done = True

        print("⇩")

        count += 1


        # add 0724
        # if count > 100:
        if count > 56:
            done = True
            break

    print("state history : {}".format(state_history))