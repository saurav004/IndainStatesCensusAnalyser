class StateCensusAnalyser:
    def __init__(self):
        self.SrNo = "SrNo"
        self.StateName = "StateName"
        self.TIN = "TIN"
        self.StateCode = "StateCode"

    def __repr__(self):
        return self.SrNo + "," + self.StateName + "," + self.TIN + "," + self.StateCode
