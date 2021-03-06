from copy import deepcopy

# DON'T CHANGE THE ORDER, only append new keys. Otherwise the numbering for the runTheMatrix tests will change.

upgradeKeys = {}

upgradeKeys[2017] = [
    '2017',
    '2017PU',
    '2017Design',
    '2017DesignPU',
]

upgradeKeys[2023] = [
    '2023D1',
    '2023D1PU',
    '2023D2',
    '2023D2PU',    
    '2023D3',    
    '2023D3PU',
    '2023D4',
    '2023D4PU',
    '2023D1Timing',
    '2023D1TimingPU',
    '2023D2Timing',
    '2023D2TimingPU',
    '2023D3Timing',
    '2023D3TimingPU',
    '2023D4Timing',
    '2023D4TimingPU',
    '2023D5',
    '2023D5PU',
    '2023D6',
    '2023D6PU'
]

upgradeSteps=[
    'GenSimFull',
    'GenSimHLBeamSpotFull',
    'GenSimHLBeamSpotFull14',
    'DigiFull',
    'RecoFullLocal',
    'RecoFullLocalPU',
    'RecoFull',
    'RecoFullGlobal',
    'RecoFullGlobalPU',
    'HARVESTFull',
    'FastSim',
    'HARVESTFast',
    'DigiFullPU',
    'RecoFullPU',
    'HARVESTFullPU',
    'RecoFull_trackingOnly',
    'RecoFull_trackingOnlyPU',
    'HARVESTFull_trackingOnly',
    'HARVESTFull_trackingOnlyPU',
    'HARVESTFullGlobal',
    'HARVESTFullGlobalPU',
    'ALCAFull'
]

upgradeProperties = {}

upgradeProperties[2017] = {
    '2017' : {
        'Geom' : 'DB:Extended',
        'GT' : 'auto:phase1_2017_realistic',
        'HLTmenu': '@relval2016',
        'Era' : 'Run2_2017',
        'ScenToRun' : ['GenSimFull','DigiFull','RecoFull','ALCAFull','HARVESTFull'],
    },
    '2017Design' : {
        'Geom' : 'DB:Extended',
        'GT' : 'auto:phase1_2017_design',
        'HLTmenu': '@relval2016',
        'Era' : 'Run2_2017',
        'BeamSpot': 'GaussSigmaZ4cm',
        'ScenToRun' : ['GenSimFull','DigiFull','RecoFull','HARVESTFull'],
    },
}

upgradeProperties[2017]['2017PU'] = deepcopy(upgradeProperties[2017]['2017'])
upgradeProperties[2017]['2017PU']['ScenToRun'] = ['GenSimFull','DigiFullPU','RecoFullPU','HARVESTFullPU']
upgradeProperties[2017]['2017DesignPU'] = deepcopy(upgradeProperties[2017]['2017Design'])
upgradeProperties[2017]['2017DesignPU']['ScenToRun'] = ['GenSimFull','DigiFullPU','RecoFullPU','HARVESTFullPU']

upgradeProperties[2023] = {
    '2023D1' : {
        'Geom' : 'Extended2023D1',
        'GT' : 'auto:phase2_realistic',
        'HLTmenu': '@fake',
        'Era' : 'Phase2C1',
        'ScenToRun' : ['GenSimHLBeamSpotFull','DigiFull','RecoFullGlobal','HARVESTFullGlobal'],
    },    
    '2023D2' : {
        'Geom' : 'Extended2023D2',
        'GT' : 'auto:phase2_realistic',
        'HLTmenu': '@fake',
        'Era' : 'Phase2C1',
        'ScenToRun' : ['GenSimHLBeamSpotFull','DigiFull','RecoFullGlobal','HARVESTFullGlobal'],
    },    
    '2023D3' : {
        'Geom' : 'Extended2023D3',
        'GT' : 'auto:phase2_realistic',
        'HLTmenu': '@fake',
        'Era' : 'Phase2C2',
        'ScenToRun' : ['GenSimHLBeamSpotFull','DigiFull','RecoFullGlobal', 'HARVESTFullGlobal'],
    },    
    '2023D4' : {
        'Geom' : 'Extended2023D4',
        'HLTmenu': '@fake',
        'GT' : 'auto:phase2_realistic',
        'Era' : 'Phase2C2',
        'ScenToRun' : ['GenSimHLBeamSpotFull','DigiFull','RecoFullGlobal', 'HARVESTFullGlobal'],
    },
    '2023D5' : {
        'Geom' : 'Extended2023D5',
        'HLTmenu': '@fake',
        'GT' : 'auto:phase2_realistic',
        'Era' : 'Phase2C2_timing',
        'ScenToRun' : ['GenSimHLBeamSpotFull','DigiFull','RecoFullGlobal', 'HARVESTFullGlobal'],
    },
    '2023D6' : {
        'Geom' : 'Extended2023D6',
        'GT' : 'auto:phase2_realistic',
        'HLTmenu': '@fake',
        'Custom' : 'SLHCUpgradeSimulations/Configuration/combinedCustoms.cust_2023tilted',
        'Era' : 'Phase2C1',
        'ScenToRun' : ['GenSimHLBeamSpotFull','DigiFull','RecoFullGlobal', 'HARVESTFullGlobal'],
    }

}



#Timing (later we can alter geometry, etc, if need be)
upgradeProperties[2023]['2023D1Timing'] = deepcopy(upgradeProperties[2023]['2023D1'])
upgradeProperties[2023]['2023D1Timing']['Era'] = 'Phase2C1_timing'
upgradeProperties[2023]['2023D2Timing'] = deepcopy(upgradeProperties[2023]['2023D2'])
upgradeProperties[2023]['2023D2Timing']['Era'] = 'Phase2C1_timing'
upgradeProperties[2023]['2023D3Timing'] = deepcopy(upgradeProperties[2023]['2023D3'])
upgradeProperties[2023]['2023D3Timing']['Era'] = 'Phase2C2_timing'
upgradeProperties[2023]['2023D4Timing'] = deepcopy(upgradeProperties[2023]['2023D4'])
upgradeProperties[2023]['2023D4Timing']['Era'] = 'Phase2C2_timing'

#standard PU sequences
upgradeProperties[2023]['2023D1PU'] = deepcopy(upgradeProperties[2023]['2023D1'])
upgradeProperties[2023]['2023D1PU']['ScenToRun'] = ['GenSimHLBeamSpotFull','DigiFullPU','RecoFullGlobalPU', 'HARVESTFullGlobalPU']
upgradeProperties[2023]['2023D2PU'] = deepcopy(upgradeProperties[2023]['2023D2'])
upgradeProperties[2023]['2023D2PU']['ScenToRun'] = ['GenSimHLBeamSpotFull','DigiFullPU','RecoFullGlobalPU', 'HARVESTFullGlobalPU']
upgradeProperties[2023]['2023D3PU'] = deepcopy(upgradeProperties[2023]['2023D3'])
upgradeProperties[2023]['2023D3PU']['ScenToRun'] = ['GenSimHLBeamSpotFull','DigiFullPU','RecoFullGlobalPU', 'HARVESTFullGlobalPU']
upgradeProperties[2023]['2023D4PU'] = deepcopy(upgradeProperties[2023]['2023D4'])
upgradeProperties[2023]['2023D4PU']['ScenToRun'] = ['GenSimHLBeamSpotFull','DigiFullPU','RecoFullGlobalPU', 'HARVESTFullGlobalPU']
upgradeProperties[2023]['2023D5PU'] = deepcopy(upgradeProperties[2023]['2023D5'])
upgradeProperties[2023]['2023D5PU']['ScenToRun'] = ['GenSimHLBeamSpotFull','DigiFullPU','RecoFullGlobalPU', 'HARVESTFullGlobalPU']
upgradeProperties[2023]['2023D6PU'] = deepcopy(upgradeProperties[2023]['2023D6'])
upgradeProperties[2023]['2023D6PU']['ScenToRun'] = ['GenSimHLBeamSpotFull','DigiFullPU','RecoFullGlobalPU', 'HARVESTFullGlobalPU']


#Timing PU (for now copy ScenToRun of standard PU)
upgradeProperties[2023]['2023D1TimingPU'] = deepcopy(upgradeProperties[2023]['2023D1Timing'])
upgradeProperties[2023]['2023D1TimingPU']['ScenToRun'] = deepcopy(upgradeProperties[2023]['2023D1PU']['ScenToRun'])
upgradeProperties[2023]['2023D2TimingPU'] = deepcopy(upgradeProperties[2023]['2023D2Timing'])
upgradeProperties[2023]['2023D2TimingPU']['ScenToRun'] = deepcopy(upgradeProperties[2023]['2023D2PU']['ScenToRun'])
upgradeProperties[2023]['2023D3TimingPU'] = deepcopy(upgradeProperties[2023]['2023D3Timing'])
upgradeProperties[2023]['2023D3TimingPU']['ScenToRun'] = deepcopy(upgradeProperties[2023]['2023D3PU']['ScenToRun'])
upgradeProperties[2023]['2023D4TimingPU'] = deepcopy(upgradeProperties[2023]['2023D4Timing'])
upgradeProperties[2023]['2023D4TimingPU']['ScenToRun'] = deepcopy(upgradeProperties[2023]['2023D4PU']['ScenToRun'])



from  Configuration.PyReleaseValidation.relval_steps import Kby

upgradeFragments=['FourMuPt_1_200_pythia8_cfi',
                  'SingleElectronPt10_cfi',
                  'SingleElectronPt35_cfi',
                  'SingleElectronPt1000_cfi',
                  'SingleGammaPt10_cfi',
                  'SingleGammaPt35_cfi',
                  'SingleMuPt1_cfi',
                  'SingleMuPt10_cfi',
                  'SingleMuPt100_cfi',
                  'SingleMuPt1000_cfi',
                  'FourMuExtendedPt_1_200_pythia8_cfi',
                  'TenMuExtendedE_0_200_pythia8_cfi',
                  'DoubleElectronPt10Extended_pythia8_cfi',
                  'DoubleElectronPt35Extended_pythia8_cfi',
                  'DoubleElectronPt1000Extended_pythia8_cfi',
                  'DoubleGammaPt10Extended_cfi',
                  'DoubleGammaPt35Extended_pythia8_cfi',
                  'DoubleMuPt1Extended_pythia8_cfi',
                  'DoubleMuPt10Extended_pythia8_cfi',
                  'DoubleMuPt100Extended_pythia8_cfi',
                  'DoubleMuPt1000Extended_pythia8_cfi',
                  'TenMuE_0_200_pythia8_cfi',
                  'SinglePiE50HCAL_cfi',
                  'MinBias_13TeV_pythia8_TuneCUETP8M1_cfi', 
                  'TTbar_13TeV_TuneCUETP8M1_cfi',
                  'ZEE_13TeV_TuneCUETP8M1_cfi',
                  'QCD_Pt_600_800_13TeV_TuneCUETP8M1_cfi',
                  'Wjet_Pt_80_120_14TeV_cfi',
                  'Wjet_Pt_3000_3500_14TeV_cfi',
                  'LM1_sfts_14TeV_cfi',
                  'QCD_Pt_3000_3500_14TeV_cfi',
                  'QCD_Pt_80_120_14TeV_cfi',
                  'H200ChargedTaus_Tauola_14TeV_cfi',
                  'JpsiMM_14TeV_cfi',
                  'TTbar_Tauola_14TeV_cfi',
                  'WE_14TeV_cfi',
                  'ZTT_Tauola_All_hadronic_14TeV_cfi',
                  'H130GGgluonfusion_14TeV_cfi',
                  'PhotonJet_Pt_10_14TeV_cfi',
                  'QQH1352T_Tauola_14TeV_cfi',
                  'MinBias_TuneZ2star_14TeV_pythia6_cff',
                  'WM_14TeV_cfi',
                  'ZMM_13TeV_TuneCUETP8M1_cfi',
                  'QCDForPF_14TeV_cfi',
                  'DYToLL_M_50_TuneZ2star_14TeV_pythia6_tauola_cff',
                  'DYtoTauTau_M_50_TuneD6T_14TeV_pythia6_tauola_cff',
                  'ZEE_14TeV_TuneCUETP8M1_cfi',
                  'QCD_Pt_80_120_13TeV_TuneCUETP8M1_cfi',
                  'H125GGgluonfusion_13TeV_TuneCUETP8M1_cfi',
]

howMuches={'FourMuPt_1_200_pythia8_cfi':Kby(10,100),
           'TenMuE_0_200_pythia8_cfi':Kby(10,100),
           'FourMuExtendedPt_1_200_pythia8_cfi':Kby(10,100),
           'TenMuExtendedE_0_200_pythia8_cfi':Kby(10,100),
           'SingleElectronPt10_cfi':Kby(9,100),
           'SingleElectronPt35_cfi':Kby(9,100),
           'SingleElectronPt1000_cfi':Kby(9,50),
           'SingleGammaPt10_cfi':Kby(9,100),
           'SingleGammaPt35_cfi':Kby(9,50),
           'SingleMuPt1_cfi':Kby(25,100),
           'SingleMuPt10_cfi':Kby(25,100),
           'SingleMuPt100_cfi':Kby(9,100),
           'SingleMuPt1000_cfi':Kby(9,100),
           'DoubleElectronPt10Extended_pythia8_cfi':Kby(9,100),
           'DoubleElectronPt35Extended_pythia8_cfi':Kby(9,100),
           'DoubleElectronPt1000Extended_pythia8_cfi':Kby(9,50),
           'DoubleGammaPt10Extended_cfi':Kby(9,100),
           'DoubleGammaPt35Extended_pythia8_cfi':Kby(9,50),
           'DoubleMuPt1Extended_pythia8_cfi':Kby(25,100),
           'DoubleMuPt10Extended_pythia8_cfi':Kby(25,100),
           'DoubleMuPt100Extended_pythia8_cfi':Kby(9,100),
           'DoubleMuPt1000Extended_pythia8_cfi':Kby(9,100),
           'SinglePiE50HCAL_cfi':Kby(10,100),
           'QCD_Pt_600_800_13TeV_TuneCUETP8M1_cfi':Kby(9,50),
           'Wjet_Pt_80_120_14TeV_cfi':Kby(9,100),
           'Wjet_Pt_3000_3500_14TeV_cfi':Kby(9,50),
           'LM1_sfts_14TeV_cfi':Kby(9,100),
           'QCD_Pt_3000_3500_14TeV_cfi':Kby(9,50),
           'QCD_Pt_80_120_14TeV_cfi':Kby(9,100),
           'H200ChargedTaus_Tauola_14TeV_cfi':Kby(9,100),
           'JpsiMM_14TeV_cfi':Kby(66,100),
           'TTbar_Tauola_14TeV_cfi':Kby(9,100),
           'WE_14TeV_cfi':Kby(9,100),
           'ZEE_13TeV_TuneCUETP8M1_cfi':Kby(9,100),
           'ZTT_Tauola_All_hadronic_14TeV_cfi':Kby(9,100),
           'H130GGgluonfusion_14TeV_cfi':Kby(9,100),
           'PhotonJet_Pt_10_14TeV_cfi':Kby(9,100),
           'QQH1352T_Tauola_14TeV_cfi':Kby(9,100),
           'MinBias_TuneZ2star_14TeV_pythia6_cff':Kby(90,100),
           'WM_14TeV_cfi':Kby(9,100),
           'ZMM_13TeV_TuneCUETP8M1_cfi':Kby(18,100),
	       'QCDForPF_14TeV_cfi':Kby(9,50),
	       'DYToLL_M_50_TuneZ2star_14TeV_pythia6_tauola_cff':Kby(9,100),
	       'DYtoTauTau_M_50_TuneD6T_14TeV_pythia6_tauola_cff':Kby(9,100),
           'TTbar_13TeV_TuneCUETP8M1_cfi':Kby(9,50),
	       'MinBias_13TeV_pythia8_TuneCUETP8M1_cfi':Kby(90,100),
           'ZEE_14TeV_TuneCUETP8M1_cfi':Kby(9,100),
           'QCD_Pt_80_120_13TeV_TuneCUETP8M1_cfi':Kby(9,100),
           'H125GGgluonfusion_13TeV_TuneCUETP8M1_cfi':Kby(9,50),
}

upgradeDatasetFromFragment={'FourMuPt_1_200_pythia8_cfi': 'FourMuPt1_200',
                            'FourMuExtendedPt_1_200_pythia8_cfi': 'FourMuExtendedPt1_200',
                            'TenMuE_0_200_pythia8_cfi': 'TenMuE_0_200',
                            'TenMuExtendedE_0_200_pythia8_cfi': 'TenMuExtendedE_0_200',
                            'SingleElectronPt10_cfi' : 'SingleElectronPt10',
                            'SingleElectronPt35_cfi' : 'SingleElectronPt35',
                            'SingleElectronPt1000_cfi' : 'SingleElectronPt1000',
                            'SingleGammaPt10_cfi' : 'SingleGammaPt10',
                            'SingleGammaPt35_cfi' : 'SingleGammaPt35',
                            'SingleMuPt1_cfi' : 'SingleMuPt1',
                            'SingleMuPt10_cfi' : 'SingleMuPt10',
                            'SingleMuPt100_cfi' : 'SingleMuPt100',
                            'SingleMuPt1000_cfi' : 'SingleMuPt1000',
                            'DoubleElectronPt10Extended_pythia8_cfi' : 'SingleElectronPt10Extended',
                            'DoubleElectronPt35Extended_pythia8_cfi' : 'SingleElectronPt35Extended',
                            'DoubleElectronPt1000Extended_pythia8_cfi' : 'SingleElectronPt1000Extended',
                            'DoubleGammaPt10Extended_cfi' : 'SingleGammaPt10Extended',
                            'DoubleGammaPt35Extended_pythia8_cfi' : 'SingleGammaPt35Extended',
                            'DoubleMuPt1Extended_pythia8_cfi' : 'SingleMuPt1Extended',
                            'DoubleMuPt10Extended_pythia8_cfi' : 'SingleMuPt10Extended',
                            'DoubleMuPt100Extended_pythia8_cfi' : 'SingleMuPt100Extended',
                            'DoubleMuPt1000Extended_pythia8_cfi' : 'SingleMuPt1000Extended',
                            'SinglePiE50HCAL_cfi' : 'SinglePiE50HCAL',
                            'QCD_Pt_600_800_13TeV_TuneCUETP8M1_cfi' : 'QCD_Pt_600_800_13',
                            'Wjet_Pt_80_120_14TeV_cfi' : 'Wjet_Pt_80_120_14TeV',
                            'Wjet_Pt_3000_3500_14TeV_cfi' : 'Wjet_Pt_3000_3500_14TeV',
                            'LM1_sfts_14TeV_cfi' : 'LM1_sfts_14TeV',
                            'QCD_Pt_3000_3500_14TeV_cfi' : 'QCD_Pt_3000_3500_14TeV',
                            'QCD_Pt_80_120_14TeV_cfi' : 'QCD_Pt_80_120_14TeV',
                            'H200ChargedTaus_Tauola_14TeV_cfi' : 'Higgs200ChargedTaus_14TeV',
                            'JpsiMM_14TeV_cfi' : 'JpsiMM_14TeV',
                            'TTbar_Tauola_14TeV_cfi' : 'TTbar_14TeV',
                            'WE_14TeV_cfi' : 'WE_14TeV',
                            'ZEE_13TeV_TuneCUETP8M1_cfi' : 'ZEE_13',
                            'ZTT_Tauola_All_hadronic_14TeV_cfi' : 'ZTT_14TeV',
                            'H130GGgluonfusion_14TeV_cfi' : 'H130GGgluonfusion_14TeV',
                            'PhotonJet_Pt_10_14TeV_cfi' : 'PhotonJets_Pt_10_14TeV',
                            'QQH1352T_Tauola_14TeV_cfi' : 'QQH1352T_Tauola_14TeV',
                            'MinBias_TuneZ2star_14TeV_pythia6_cff' : 'MinBias_TuneZ2star_14TeV',
                            'WM_14TeV_cfi' : 'WM_14TeV',
                            'ZMM_13TeV_TuneCUETP8M1_cfi' : 'ZMM_13',
                            'QCDForPF_14TeV_cfi' : 'QCDForPF_14TeV',
                            'DYToLL_M_50_TuneZ2star_14TeV_pythia6_tauola_cff' : 'DYToLL_M_50_TuneZ2star_14TeV',
                            'DYtoTauTau_M_50_TuneD6T_14TeV_pythia6_tauola_cff' : 'DYtoTauTau_M_50_TuneD6T_14TeV',
                            'TTbar_13TeV_TuneCUETP8M1_cfi' : 'TTbar_13',
                            'MinBias_13TeV_pythia8_TuneCUETP8M1_cfi' : 'MinBias_13',
                            'ZEE_14TeV_TuneCUETP8M1_cfi' : 'ZEE_14',
                            'QCD_Pt_80_120_13TeV_TuneCUETP8M1_cfi' : 'QCD_Pt_80_120_13',
                            'H125GGgluonfusion_13TeV_TuneCUETP8M1_cfi' : 'H125GGgluonfusion_13',
}
