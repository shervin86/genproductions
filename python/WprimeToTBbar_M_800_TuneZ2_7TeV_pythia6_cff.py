## Wprime to muon, Z2 tune, 38x production


import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

from Configuration.Generator.PythiaUEZ2Settings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.),
    crossSection = cms.untracked.double(0.56),
    comEnergy = cms.double(7000.0),
    PythiaParameters = cms.PSet(
       pythiaUESettings = cms.vstring(
            'MSTJ(11)=3      ! Choice of the fragmentation function', 
            'MSTJ(22)=2      ! Decay those unstable particles', 
            'PARJ(71)=10.    ! for which ctau  10 mm', 
            'MSTP(2)=1       ! which order running alphaS', 
            'MSTP(33)=0      ! no K factors in hard cross sections', 
            'MSTP(51)=7      ! structure function chosen', 
            'MSTP(81)=1      ! multiple parton interactions 1 is Pythia default', 
            'MSTP(82)=4      ! Defines the multi-parton model', 
            'MSTU(21)=1      ! Check on possible errors during program execution', 
            'PARP(82)=1.9409 ! pt cutoff for multiparton interactions', 
            'PARP(89)=1960.  ! sqrts for which PARP82 is set', 
            'PARP(83)=0.5    ! Multiple interactions: matter distrbn parameter', 
            'PARP(84)=0.4    ! Multiple interactions: matter distribution parameter', 
            'PARP(90)=0.16   ! Multiple interactions: rescaling power', 
            'PARP(67)=2.5    ! amount of initial-state radiation', 
            'PARP(85)=1.0    ! gluon prod. mechanism in MI', 
            'PARP(86)=1.0    ! gluon prod. mechanism in MI', 
            'PARP(62)=1.25   ! ', 
            'PARP(64)=0.2    ! ', 
            'MSTP(91)=1      !', 
            'PARP(91)=2.1    ! kt distribution', 
            'PARP(93)=15.0   ! '),
       processParameters = cms.vstring('MSEL        = 0    !User defined processes', 
                                        'MSUB(142)   = 1    !Wprime  production',
                                        'PMAS(34,1)  = 800.!mass of Wprime',
                                        'PMAS(34,2)  = 24.  !width of Wprime',
                                        'MDME(311,1) = 0    !W\' decay into dbar u', 
                                        'MDME(312,1) = 0    !W\' decay into dbar c', 
                                        'MDME(313,1) = 0    !W\' decay into dbar t', 
                                        'MDME(315,1) = 0    !W\' decay into sbar u', 
                                        'MDME(316,1) = 0    !W\' decay into sbar c', 
                                        'MDME(317,1) = 0    !W\' decay into sbar t', 
                                        'MDME(319,1) = 0    !W\' decay into bbar u', 
                                        'MDME(320,1) = 0    !W\' decay into bbar c', 
                                        'MDME(321,1) = 1    !W\' decay into bbar t', 
                                        'MDME(327,1) = 0    !W\' decay into e+ nu_e', 
                                        'MDME(328,1) = 0    !W\' decay into mu+ nu_mu', 
                                        'MDME(329,1) = 0    !W\' decay into tau+ nu_tau'),
       # This is a vector of ParameterSet names to be read, in this order
       parameterSets = cms.vstring('pythiaUESettings', 
                                   'processParameters')
    )
)




ProductionFilterSequence = cms.Sequence(generator)
