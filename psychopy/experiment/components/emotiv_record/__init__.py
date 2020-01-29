# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 11:20:49 2017

@author: mrbki
"""
from os import path
from psychopy.experiment.components import BaseComponent, getInitVals
from psychopy.localization import _translate


OBJECT_NAME = 'cortex_obj'

thisFolder = path.abspath(path.dirname(__file__))
iconFile = path.join(thisFolder, 'emotiv.jpg')
tooltip = _translate('Initialize EMOTIV hardware connection')


class EmotivRecordingComponent(BaseComponent):  # or (VisualComponent)
    def __init__(self, exp, parentName, name='cortex_rec'):
        super(EmotivRecordingComponent, self).__init__(
            exp, parentName, name=name,
            startType='time (s)', startVal=0,
            stopType='duration (s)', stopVal="",
            startEstim='', durationEstim='',
            saveStartStop=False
        )
        self.exp.requirePsychopyLibs(['emotiv'])

    def writeInitCode(self, buff):
        inits = getInitVals(self.params, 'PsychoPy')
        code = ('{} = visual.BaseVisualStim('.format(inits['name']) +
                'win=win, name="{}")\n'.format(inits['name'])
                )
        buff.writeIndentedLines(code)
        code = ('{} = emotiv.Cortex()\n'.format(OBJECT_NAME))
        buff.writeIndentedLines(code)

    def writeFrameCode(self, buff):
        pass

    def writeExperimentEndCode(self, buff):
        code = (
                "core.wait(1) # Wait for EEG data to be packaged\n" +
                "{}.close_session()\n".format(OBJECT_NAME)
        )
        buff.writeIndentedLines(code)
