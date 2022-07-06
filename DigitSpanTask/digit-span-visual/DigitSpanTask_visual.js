/***************************** 
 * Digitspantask_Visual Test *
 *****************************/

import { core, data, sound, util, visual } from './lib/psychojs-2022.1.3.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'DigitSpanTask_visual';  // from the Builder filename that created this script
let expInfo = {'participante': '', 'sesion': '01', 'orden': ["AP", "PA"], 'pasivas': ["RF", "FR"], 'activas': ["RF", "FR"]};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(BienvenidaRoutineBegin());
flowScheduler.add(BienvenidaRoutineEachFrame());
flowScheduler.add(BienvenidaRoutineEnd());
flowScheduler.add(Bienvenida2RoutineBegin());
flowScheduler.add(Bienvenida2RoutineEachFrame());
flowScheduler.add(Bienvenida2RoutineEnd());
const Block_OrderLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Block_OrderLoopBegin(Block_OrderLoopScheduler));
flowScheduler.add(Block_OrderLoopScheduler);
flowScheduler.add(Block_OrderLoopEnd);
flowScheduler.add(FinalRoutineBegin());
flowScheduler.add(FinalRoutineEachFrame());
flowScheduler.add(FinalRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'datasets/trial_init.wav', 'path': 'datasets/trial_init.wav'},
    {'name': 'datasets/instructions.xlsx', 'path': 'datasets/instructions.xlsx'},
    {'name': 'datasets/instruccion2.png', 'path': 'datasets/instruccion2.png'},
    {'name': 'datasets/instruccion1_activa.png', 'path': 'datasets/instruccion1_activa.png'},
    {'name': 'datasets/instruccion1_pasiva.png', 'path': 'datasets/instruccion1_pasiva.png'},
    {'name': 'datasets/drift.png', 'path': 'datasets/drift.png'},
    {'name': 'datasets/task_order.xlsx', 'path': 'datasets/task_order.xlsx'},
    {'name': 'datasets/Bienvenida.png', 'path': 'datasets/Bienvenida.png'},
    {'name': 'datasets/finpractica.png', 'path': 'datasets/finpractica.png'},
    {'name': 'datasets/instruccion3.png', 'path': 'datasets/instruccion3.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.3';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participante"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var BienvenidaClock;
var key_bienvenida;
var Bienvenida_img;
var ordenactivas;
var ordenpasivas;
var lasfilas;
var Bienvenida2Clock;
var bienv2;
var key_bienv;
var InstruccionesPasivaClock;
var image2;
var key_resp_2;
var firstfix_trainingClock;
var drift_trainPR;
var start_trainPR;
var firstfixtrain;
var presentation_trainingClock;
var digitpresentation_training;
var recall_trainingClock;
var recall_train;
var answ_train;
var post_recall_trainClock;
var post_recall_training;
var start_trialClock;
var end_training;
var key_resp;
var first_fixationClock;
var driftPR;
var startPR;
var first_fix_pas;
var Presentation_pasClock;
var pres_text;
var Recall_pasivasClock;
var recall_txt;
var answer_box;
var previous_count;
var current_count;
var post_recallPasivaClock;
var postrecallPR;
var LickertPasivasClock;
var Dificultad_pasivas;
var dif_licker;
var EndTaskClock;
var siguiente_tarea;
var key_resp_6;
var Instr_ActivasClock;
var image2_2;
var key_resp_3;
var drift_press_activasClock;
var start_trainPR_2;
var drift_trainPR_2;
var firstfix_activas;
var key_resp_5;
var ffix_trainactivasClock;
var firsfixtrain_activa;
var present_train_activasClock;
var digitpresentation_training_2;
var recall_train_activasClock;
var recall_train_2;
var answ_train_2;
var post_recall_train_activasClock;
var post_recall_training_2;
var start_trialActivasClock;
var end_training_2;
var key_resp_4;
var first_fixActivasClock;
var first_fix_active;
var PresentationActivasClock;
var pres_text_active;
var RecallActivasClock;
var recall_txt_2;
var answer_box_2;
var post_recallActivasClock;
var postrecallPR_2;
var LickertActivasClock;
var Dificultad_activas;
var dif_licker_2;
var FinalClock;
var text_2;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Bienvenida"
  BienvenidaClock = new util.Clock();
  key_bienvenida = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Bienvenida_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Bienvenida_img', units : undefined, 
    image : 'datasets/Bienvenida.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  if ((expInfo["activas"] === "RF")) {
      ordenactivas = ["AR", "AF"];
  } else {
      ordenactivas = ["AF", "AR"];
  }
  if ((expInfo["pasivas"] === "RF")) {
      ordenpasivas = ["PR", "PF"];
  } else {
      ordenpasivas = ["PF", "PR"];
  }
  if ((expInfo["orden"] === "AP")) {
      lasfilas = [0, 1];
  } else {
      lasfilas = [1, 2];
  }
  
  // Initialize components for Routine "Bienvenida2"
  Bienvenida2Clock = new util.Clock();
  bienv2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'bienv2',
    text: 'Este experimento consta de 4 tareas cortas.\nEn cada tarea, verás una serie de números que debes recordar. \n\nA continuación, verás las instrucciones de la primera tarea.\n\n*Presiona la barra espaciadora para seguir*',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  key_bienv = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "InstruccionesPasiva"
  InstruccionesPasivaClock = new util.Clock();
  image2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "firstfix_training"
  firstfix_trainingClock = new util.Clock();
  drift_trainPR = new visual.ImageStim({
    win : psychoJS.window,
    name : 'drift_trainPR', units : undefined, 
    image : 'datasets/drift.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  start_trainPR = new sound.Sound({
    win: psychoJS.window,
    value: 'datasets/trial_init.wav',
    secs: 0.5,
    });
  start_trainPR.setVolume(1.0);
  firstfixtrain = new visual.TextStim({
    win: psychoJS.window,
    name: 'firstfixtrain',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "presentation_training"
  presentation_trainingClock = new util.Clock();
  digitpresentation_training = new visual.TextStim({
    win: psychoJS.window,
    name: 'digitpresentation_training',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "recall_training"
  recall_trainingClock = new util.Clock();
  recall_train = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_train',
    text: 'Respuesta:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  answ_train = new visual.TextBox({
    win: psychoJS.window,
    name: 'answ_train',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: 0.1,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "post_recall_train"
  post_recall_trainClock = new util.Clock();
  post_recall_training = new visual.TextStim({
    win: psychoJS.window,
    name: 'post_recall_training',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "start_trial"
  start_trialClock = new util.Clock();
  end_training = new visual.ImageStim({
    win : psychoJS.window,
    name : 'end_training', units : undefined, 
    image : 'datasets/finpractica.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_fixation"
  first_fixationClock = new util.Clock();
  driftPR = new visual.ImageStim({
    win : psychoJS.window,
    name : 'driftPR', units : undefined, 
    image : 'datasets/drift.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  startPR = new sound.Sound({
    win: psychoJS.window,
    value: 'datasets/trial_init.wav',
    secs: 0.5,
    });
  startPR.setVolume(1.0);
  first_fix_pas = new visual.TextStim({
    win: psychoJS.window,
    name: 'first_fix_pas',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Presentation_pas"
  Presentation_pasClock = new util.Clock();
  pres_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'pres_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Recall_pasivas"
  Recall_pasivasClock = new util.Clock();
  recall_txt = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txt',
    text: 'Respuesta:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  answer_box = new visual.TextBox({
    win: psychoJS.window,
    name: 'answer_box',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: 0.1,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  previous_count = 0;
  current_count = 0;
  
  // Initialize components for Routine "post_recallPasiva"
  post_recallPasivaClock = new util.Clock();
  postrecallPR = new visual.TextStim({
    win: psychoJS.window,
    name: 'postrecallPR',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "LickertPasivas"
  LickertPasivasClock = new util.Clock();
  Dificultad_pasivas = new visual.TextStim({
    win: psychoJS.window,
    name: 'Dificultad_pasivas',
    text: '¿Cuán difícil encontraste esta tarea, en general?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  dif_licker = new visual.Slider({
    win: psychoJS.window, name: 'dif_licker',
    size: [1.0, 0.1], pos: [0, 0], units: 'height',
    labels: ["muy f\u00e1cil", "f\u00e1cil", "neutro", "dif\u00edcil", "muy dif\u00edcil"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 0.0, style: ["RADIO"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color([1.0, 0.2941, (- 1.0)]), lineColor: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "EndTask"
  EndTaskClock = new util.Clock();
  siguiente_tarea = new visual.TextStim({
    win: psychoJS.window,
    name: 'siguiente_tarea',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Instr_Activas"
  Instr_ActivasClock = new util.Clock();
  image2_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image2_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "drift_press_activas"
  drift_press_activasClock = new util.Clock();
  start_trainPR_2 = new sound.Sound({
    win: psychoJS.window,
    value: 'datasets/trial_init.wav',
    secs: 0.5,
    });
  start_trainPR_2.setVolume(1.0);
  drift_trainPR_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'drift_trainPR_2', units : undefined, 
    image : 'datasets/drift.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  firstfix_activas = new visual.TextStim({
    win: psychoJS.window,
    name: 'firstfix_activas',
    text: '+',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ffix_trainactivas"
  ffix_trainactivasClock = new util.Clock();
  firsfixtrain_activa = new visual.TextStim({
    win: psychoJS.window,
    name: 'firsfixtrain_activa',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "present_train_activas"
  present_train_activasClock = new util.Clock();
  digitpresentation_training_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'digitpresentation_training_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "recall_train_activas"
  recall_train_activasClock = new util.Clock();
  recall_train_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_train_2',
    text: 'Respuesta:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  answ_train_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'answ_train_2',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: 0.1,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "post_recall_train_activas"
  post_recall_train_activasClock = new util.Clock();
  post_recall_training_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'post_recall_training_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "start_trialActivas"
  start_trialActivasClock = new util.Clock();
  end_training_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'end_training_2', units : undefined, 
    image : 'datasets/finpractica.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "first_fixActivas"
  first_fixActivasClock = new util.Clock();
  first_fix_active = new visual.TextStim({
    win: psychoJS.window,
    name: 'first_fix_active',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PresentationActivas"
  PresentationActivasClock = new util.Clock();
  pres_text_active = new visual.TextStim({
    win: psychoJS.window,
    name: 'pres_text_active',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "RecallActivas"
  RecallActivasClock = new util.Clock();
  recall_txt_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'recall_txt_2',
    text: 'Respuesta:',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  answer_box_2 = new visual.TextBox({
    win: psychoJS.window,
    name: 'answer_box_2',
    text: '',
    font: 'Arial',
    pos: [0, 0], letterHeight: 0.1,
    size: [null, null],  units: undefined, 
    color: 'white', colorSpace: 'rgb',
    fillColor: undefined, borderColor: undefined,
    bold: false, italic: false,
    opacity: undefined,
    padding: 0.0,
    editable: true,
    multiline: true,
    anchor: 'center',
    depth: -1.0 
  });
  
  // Initialize components for Routine "post_recallActivas"
  post_recallActivasClock = new util.Clock();
  postrecallPR_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'postrecallPR_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "LickertActivas"
  LickertActivasClock = new util.Clock();
  Dificultad_activas = new visual.TextStim({
    win: psychoJS.window,
    name: 'Dificultad_activas',
    text: '¿Cuán difícil encontraste esta tarea, en general?',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0.25], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  dif_licker_2 = new visual.Slider({
    win: psychoJS.window, name: 'dif_licker_2',
    size: [1.0, 0.1], pos: [0, 0], units: 'height',
    labels: ["muy f\u00e1cil", "f\u00e1cil", "neutro", "dif\u00edcil", "muy dif\u00edcil"], fontSize: 0.05, ticks: [1, 2, 3, 4, 5],
    granularity: 0.0, style: ["RADIO"],
    color: new util.Color([1.0, 1.0, 1.0]), markerColor: new util.Color([1.0, 0.2941, (- 1.0)]), lineColor: new util.Color('White'), 
    fontFamily: 'Arial', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  // Initialize components for Routine "Final"
  FinalClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '¡Hemos terminado!\n\n¡Muchas gracias por tu participación!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _key_bienvenida_allKeys;
var BienvenidaComponents;
function BienvenidaRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Bienvenida'-------
    t = 0;
    BienvenidaClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_bienvenida.keys = undefined;
    key_bienvenida.rt = undefined;
    _key_bienvenida_allKeys = [];
    // keep track of which components have finished
    BienvenidaComponents = [];
    BienvenidaComponents.push(key_bienvenida);
    BienvenidaComponents.push(Bienvenida_img);
    
    for (const thisComponent of BienvenidaComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function BienvenidaRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Bienvenida'-------
    // get current time
    t = BienvenidaClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *key_bienvenida* updates
    if (t >= 0.25 && key_bienvenida.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_bienvenida.tStart = t;  // (not accounting for frame time here)
      key_bienvenida.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      key_bienvenida.clock.reset();
      key_bienvenida.start();
      key_bienvenida.clearEvents();
    }

    if (key_bienvenida.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_bienvenida.getKeys({keyList: ['space'], waitRelease: false});
      _key_bienvenida_allKeys = _key_bienvenida_allKeys.concat(theseKeys);
      if (_key_bienvenida_allKeys.length > 0) {
        key_bienvenida.keys = _key_bienvenida_allKeys[_key_bienvenida_allKeys.length - 1].name;  // just the last key pressed
        key_bienvenida.rt = _key_bienvenida_allKeys[_key_bienvenida_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *Bienvenida_img* updates
    if (t >= 0.0 && Bienvenida_img.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Bienvenida_img.tStart = t;  // (not accounting for frame time here)
      Bienvenida_img.frameNStart = frameN;  // exact frame index
      
      Bienvenida_img.setAutoDraw(true);
    }

    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of BienvenidaComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function BienvenidaRoutineEnd() {
  return async function () {
    //------Ending Routine 'Bienvenida'-------
    for (const thisComponent of BienvenidaComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_bienvenida.stop();
    // the Routine "Bienvenida" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_bienv_allKeys;
var Bienvenida2Components;
function Bienvenida2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Bienvenida2'-------
    t = 0;
    Bienvenida2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_bienv.keys = undefined;
    key_bienv.rt = undefined;
    _key_bienv_allKeys = [];
    // keep track of which components have finished
    Bienvenida2Components = [];
    Bienvenida2Components.push(bienv2);
    Bienvenida2Components.push(key_bienv);
    
    for (const thisComponent of Bienvenida2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Bienvenida2RoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Bienvenida2'-------
    // get current time
    t = Bienvenida2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *bienv2* updates
    if (t >= 0.0 && bienv2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      bienv2.tStart = t;  // (not accounting for frame time here)
      bienv2.frameNStart = frameN;  // exact frame index
      
      bienv2.setAutoDraw(true);
    }

    
    // *key_bienv* updates
    if (t >= 0.25 && key_bienv.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_bienv.tStart = t;  // (not accounting for frame time here)
      key_bienv.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_bienv.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_bienv.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_bienv.clearEvents(); });
    }

    if (key_bienv.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_bienv.getKeys({keyList: ['space'], waitRelease: false});
      _key_bienv_allKeys = _key_bienv_allKeys.concat(theseKeys);
      if (_key_bienv_allKeys.length > 0) {
        key_bienv.keys = _key_bienv_allKeys[_key_bienv_allKeys.length - 1].name;  // just the last key pressed
        key_bienv.rt = _key_bienv_allKeys[_key_bienv_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Bienvenida2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Bienvenida2RoutineEnd() {
  return async function () {
    //------Ending Routine 'Bienvenida2'-------
    for (const thisComponent of Bienvenida2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_bienv.corr, level);
    }
    psychoJS.experiment.addData('key_bienv.keys', key_bienv.keys);
    if (typeof key_bienv.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_bienv.rt', key_bienv.rt);
        routineTimer.reset();
        }
    
    key_bienv.stop();
    // the Routine "Bienvenida2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Block_Order;
var currentLoop;
function Block_OrderLoopBegin(Block_OrderLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    Block_Order = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: TrialHandler.importConditions(psychoJS.serverManager, 'datasets/task_order.xlsx', lasfilas),
      seed: undefined, name: 'Block_Order'
    });
    psychoJS.experiment.addLoop(Block_Order); // add the loop to the experiment
    currentLoop = Block_Order;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlock_Order of Block_Order) {
      const snapshot = Block_Order.getSnapshot();
      Block_OrderLoopScheduler.add(importConditions(snapshot));
      const BlockPasivasLoopScheduler = new Scheduler(psychoJS);
      Block_OrderLoopScheduler.add(BlockPasivasLoopBegin(BlockPasivasLoopScheduler, snapshot));
      Block_OrderLoopScheduler.add(BlockPasivasLoopScheduler);
      Block_OrderLoopScheduler.add(BlockPasivasLoopEnd);
      const BlockActivasLoopScheduler = new Scheduler(psychoJS);
      Block_OrderLoopScheduler.add(BlockActivasLoopBegin(BlockActivasLoopScheduler, snapshot));
      Block_OrderLoopScheduler.add(BlockActivasLoopScheduler);
      Block_OrderLoopScheduler.add(BlockActivasLoopEnd);
      Block_OrderLoopScheduler.add(endLoopIteration(Block_OrderLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var BlockPasivas;
function BlockPasivasLoopBegin(BlockPasivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    BlockPasivas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nRepsBlockPasivas, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'BlockPasivas'
    });
    psychoJS.experiment.addLoop(BlockPasivas); // add the loop to the experiment
    currentLoop = BlockPasivas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlockPasiva of BlockPasivas) {
      const snapshot = BlockPasivas.getSnapshot();
      BlockPasivasLoopScheduler.add(importConditions(snapshot));
      const instrucloop_PasivasLoopScheduler = new Scheduler(psychoJS);
      BlockPasivasLoopScheduler.add(instrucloop_PasivasLoopBegin(instrucloop_PasivasLoopScheduler, snapshot));
      BlockPasivasLoopScheduler.add(instrucloop_PasivasLoopScheduler);
      BlockPasivasLoopScheduler.add(instrucloop_PasivasLoopEnd);
      const trial_trainingPasivasLoopScheduler = new Scheduler(psychoJS);
      BlockPasivasLoopScheduler.add(trial_trainingPasivasLoopBegin(trial_trainingPasivasLoopScheduler, snapshot));
      BlockPasivasLoopScheduler.add(trial_trainingPasivasLoopScheduler);
      BlockPasivasLoopScheduler.add(trial_trainingPasivasLoopEnd);
      BlockPasivasLoopScheduler.add(start_trialRoutineBegin(snapshot));
      BlockPasivasLoopScheduler.add(start_trialRoutineEachFrame());
      BlockPasivasLoopScheduler.add(start_trialRoutineEnd());
      const trial_PasivaLoopScheduler = new Scheduler(psychoJS);
      BlockPasivasLoopScheduler.add(trial_PasivaLoopBegin(trial_PasivaLoopScheduler, snapshot));
      BlockPasivasLoopScheduler.add(trial_PasivaLoopScheduler);
      BlockPasivasLoopScheduler.add(trial_PasivaLoopEnd);
      BlockPasivasLoopScheduler.add(LickertPasivasRoutineBegin(snapshot));
      BlockPasivasLoopScheduler.add(LickertPasivasRoutineEachFrame());
      BlockPasivasLoopScheduler.add(LickertPasivasRoutineEnd());
      BlockPasivasLoopScheduler.add(EndTaskRoutineBegin(snapshot));
      BlockPasivasLoopScheduler.add(EndTaskRoutineEachFrame());
      BlockPasivasLoopScheduler.add(EndTaskRoutineEnd());
      BlockPasivasLoopScheduler.add(endLoopIteration(BlockPasivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var instrucloop_Pasivas;
function instrucloop_PasivasLoopBegin(instrucloop_PasivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    instrucloop_Pasivas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'datasets/instructions.xlsx',
      seed: undefined, name: 'instrucloop_Pasivas'
    });
    psychoJS.experiment.addLoop(instrucloop_Pasivas); // add the loop to the experiment
    currentLoop = instrucloop_Pasivas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisInstrucloop_Pasiva of instrucloop_Pasivas) {
      const snapshot = instrucloop_Pasivas.getSnapshot();
      instrucloop_PasivasLoopScheduler.add(importConditions(snapshot));
      instrucloop_PasivasLoopScheduler.add(InstruccionesPasivaRoutineBegin(snapshot));
      instrucloop_PasivasLoopScheduler.add(InstruccionesPasivaRoutineEachFrame());
      instrucloop_PasivasLoopScheduler.add(InstruccionesPasivaRoutineEnd());
      instrucloop_PasivasLoopScheduler.add(endLoopIteration(instrucloop_PasivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function instrucloop_PasivasLoopEnd() {
  psychoJS.experiment.removeLoop(instrucloop_Pasivas);

  return Scheduler.Event.NEXT;
}


var trial_trainingPasivas;
function trial_trainingPasivasLoopBegin(trial_trainingPasivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trial_trainingPasivas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: (("datasets/training_" + ordenpasivas[BlockPasivas.thisN]) + ".xlsx"),
      seed: undefined, name: 'trial_trainingPasivas'
    });
    psychoJS.experiment.addLoop(trial_trainingPasivas); // add the loop to the experiment
    currentLoop = trial_trainingPasivas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_trainingPasiva of trial_trainingPasivas) {
      const snapshot = trial_trainingPasivas.getSnapshot();
      trial_trainingPasivasLoopScheduler.add(importConditions(snapshot));
      trial_trainingPasivasLoopScheduler.add(firstfix_trainingRoutineBegin(snapshot));
      trial_trainingPasivasLoopScheduler.add(firstfix_trainingRoutineEachFrame());
      trial_trainingPasivasLoopScheduler.add(firstfix_trainingRoutineEnd());
      const train_digitloopPasivasLoopScheduler = new Scheduler(psychoJS);
      trial_trainingPasivasLoopScheduler.add(train_digitloopPasivasLoopBegin(train_digitloopPasivasLoopScheduler, snapshot));
      trial_trainingPasivasLoopScheduler.add(train_digitloopPasivasLoopScheduler);
      trial_trainingPasivasLoopScheduler.add(train_digitloopPasivasLoopEnd);
      trial_trainingPasivasLoopScheduler.add(recall_trainingRoutineBegin(snapshot));
      trial_trainingPasivasLoopScheduler.add(recall_trainingRoutineEachFrame());
      trial_trainingPasivasLoopScheduler.add(recall_trainingRoutineEnd());
      trial_trainingPasivasLoopScheduler.add(post_recall_trainRoutineBegin(snapshot));
      trial_trainingPasivasLoopScheduler.add(post_recall_trainRoutineEachFrame());
      trial_trainingPasivasLoopScheduler.add(post_recall_trainRoutineEnd());
      trial_trainingPasivasLoopScheduler.add(endLoopIteration(trial_trainingPasivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var train_digitloopPasivas;
function train_digitloopPasivasLoopBegin(train_digitloopPasivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    train_digitloopPasivas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan_train, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'train_digitloopPasivas'
    });
    psychoJS.experiment.addLoop(train_digitloopPasivas); // add the loop to the experiment
    currentLoop = train_digitloopPasivas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrain_digitloopPasiva of train_digitloopPasivas) {
      const snapshot = train_digitloopPasivas.getSnapshot();
      train_digitloopPasivasLoopScheduler.add(importConditions(snapshot));
      train_digitloopPasivasLoopScheduler.add(presentation_trainingRoutineBegin(snapshot));
      train_digitloopPasivasLoopScheduler.add(presentation_trainingRoutineEachFrame());
      train_digitloopPasivasLoopScheduler.add(presentation_trainingRoutineEnd());
      train_digitloopPasivasLoopScheduler.add(endLoopIteration(train_digitloopPasivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function train_digitloopPasivasLoopEnd() {
  psychoJS.experiment.removeLoop(train_digitloopPasivas);

  return Scheduler.Event.NEXT;
}


async function trial_trainingPasivasLoopEnd() {
  psychoJS.experiment.removeLoop(trial_trainingPasivas);

  return Scheduler.Event.NEXT;
}


var trial_Pasiva;
function trial_PasivaLoopBegin(trial_PasivaLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trial_Pasiva = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: (("datasets/Dataset_" + ordenpasivas[BlockPasivas.thisN]) + ".xlsx"),
      seed: undefined, name: 'trial_Pasiva'
    });
    psychoJS.experiment.addLoop(trial_Pasiva); // add the loop to the experiment
    currentLoop = trial_Pasiva;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_Pasiva of trial_Pasiva) {
      const snapshot = trial_Pasiva.getSnapshot();
      trial_PasivaLoopScheduler.add(importConditions(snapshot));
      trial_PasivaLoopScheduler.add(first_fixationRoutineBegin(snapshot));
      trial_PasivaLoopScheduler.add(first_fixationRoutineEachFrame());
      trial_PasivaLoopScheduler.add(first_fixationRoutineEnd());
      const digitLoop_PasivasLoopScheduler = new Scheduler(psychoJS);
      trial_PasivaLoopScheduler.add(digitLoop_PasivasLoopBegin(digitLoop_PasivasLoopScheduler, snapshot));
      trial_PasivaLoopScheduler.add(digitLoop_PasivasLoopScheduler);
      trial_PasivaLoopScheduler.add(digitLoop_PasivasLoopEnd);
      trial_PasivaLoopScheduler.add(Recall_pasivasRoutineBegin(snapshot));
      trial_PasivaLoopScheduler.add(Recall_pasivasRoutineEachFrame());
      trial_PasivaLoopScheduler.add(Recall_pasivasRoutineEnd());
      trial_PasivaLoopScheduler.add(post_recallPasivaRoutineBegin(snapshot));
      trial_PasivaLoopScheduler.add(post_recallPasivaRoutineEachFrame());
      trial_PasivaLoopScheduler.add(post_recallPasivaRoutineEnd());
      trial_PasivaLoopScheduler.add(endLoopIteration(trial_PasivaLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var digitLoop_Pasivas;
function digitLoop_PasivasLoopBegin(digitLoop_PasivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    digitLoop_Pasivas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'digitLoop_Pasivas'
    });
    psychoJS.experiment.addLoop(digitLoop_Pasivas); // add the loop to the experiment
    currentLoop = digitLoop_Pasivas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoop_Pasiva of digitLoop_Pasivas) {
      const snapshot = digitLoop_Pasivas.getSnapshot();
      digitLoop_PasivasLoopScheduler.add(importConditions(snapshot));
      digitLoop_PasivasLoopScheduler.add(Presentation_pasRoutineBegin(snapshot));
      digitLoop_PasivasLoopScheduler.add(Presentation_pasRoutineEachFrame());
      digitLoop_PasivasLoopScheduler.add(Presentation_pasRoutineEnd());
      digitLoop_PasivasLoopScheduler.add(endLoopIteration(digitLoop_PasivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function digitLoop_PasivasLoopEnd() {
  psychoJS.experiment.removeLoop(digitLoop_Pasivas);

  return Scheduler.Event.NEXT;
}


async function trial_PasivaLoopEnd() {
  psychoJS.experiment.removeLoop(trial_Pasiva);

  return Scheduler.Event.NEXT;
}


async function BlockPasivasLoopEnd() {
  psychoJS.experiment.removeLoop(BlockPasivas);

  return Scheduler.Event.NEXT;
}


var BlockActivas;
function BlockActivasLoopBegin(BlockActivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    BlockActivas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: nRepsBlockActivas, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'BlockActivas'
    });
    psychoJS.experiment.addLoop(BlockActivas); // add the loop to the experiment
    currentLoop = BlockActivas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisBlockActiva of BlockActivas) {
      const snapshot = BlockActivas.getSnapshot();
      BlockActivasLoopScheduler.add(importConditions(snapshot));
      const intrLoopActivasLoopScheduler = new Scheduler(psychoJS);
      BlockActivasLoopScheduler.add(intrLoopActivasLoopBegin(intrLoopActivasLoopScheduler, snapshot));
      BlockActivasLoopScheduler.add(intrLoopActivasLoopScheduler);
      BlockActivasLoopScheduler.add(intrLoopActivasLoopEnd);
      const trial_train_ActivasLoopScheduler = new Scheduler(psychoJS);
      BlockActivasLoopScheduler.add(trial_train_ActivasLoopBegin(trial_train_ActivasLoopScheduler, snapshot));
      BlockActivasLoopScheduler.add(trial_train_ActivasLoopScheduler);
      BlockActivasLoopScheduler.add(trial_train_ActivasLoopEnd);
      BlockActivasLoopScheduler.add(start_trialActivasRoutineBegin(snapshot));
      BlockActivasLoopScheduler.add(start_trialActivasRoutineEachFrame());
      BlockActivasLoopScheduler.add(start_trialActivasRoutineEnd());
      const trialActivasLoopScheduler = new Scheduler(psychoJS);
      BlockActivasLoopScheduler.add(trialActivasLoopBegin(trialActivasLoopScheduler, snapshot));
      BlockActivasLoopScheduler.add(trialActivasLoopScheduler);
      BlockActivasLoopScheduler.add(trialActivasLoopEnd);
      BlockActivasLoopScheduler.add(LickertActivasRoutineBegin(snapshot));
      BlockActivasLoopScheduler.add(LickertActivasRoutineEachFrame());
      BlockActivasLoopScheduler.add(LickertActivasRoutineEnd());
      BlockActivasLoopScheduler.add(EndTaskRoutineBegin(snapshot));
      BlockActivasLoopScheduler.add(EndTaskRoutineEachFrame());
      BlockActivasLoopScheduler.add(EndTaskRoutineEnd());
      BlockActivasLoopScheduler.add(endLoopIteration(BlockActivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var intrLoopActivas;
function intrLoopActivasLoopBegin(intrLoopActivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    intrLoopActivas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'datasets/instructions.xlsx',
      seed: undefined, name: 'intrLoopActivas'
    });
    psychoJS.experiment.addLoop(intrLoopActivas); // add the loop to the experiment
    currentLoop = intrLoopActivas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisIntrLoopActiva of intrLoopActivas) {
      const snapshot = intrLoopActivas.getSnapshot();
      intrLoopActivasLoopScheduler.add(importConditions(snapshot));
      intrLoopActivasLoopScheduler.add(Instr_ActivasRoutineBegin(snapshot));
      intrLoopActivasLoopScheduler.add(Instr_ActivasRoutineEachFrame());
      intrLoopActivasLoopScheduler.add(Instr_ActivasRoutineEnd());
      intrLoopActivasLoopScheduler.add(endLoopIteration(intrLoopActivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function intrLoopActivasLoopEnd() {
  psychoJS.experiment.removeLoop(intrLoopActivas);

  return Scheduler.Event.NEXT;
}


var trial_train_Activas;
function trial_train_ActivasLoopBegin(trial_train_ActivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trial_train_Activas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: (("datasets/training_" + ordenactivas[BlockActivas.thisN]) + ".xlsx"),
      seed: undefined, name: 'trial_train_Activas'
    });
    psychoJS.experiment.addLoop(trial_train_Activas); // add the loop to the experiment
    currentLoop = trial_train_Activas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrial_train_Activa of trial_train_Activas) {
      const snapshot = trial_train_Activas.getSnapshot();
      trial_train_ActivasLoopScheduler.add(importConditions(snapshot));
      trial_train_ActivasLoopScheduler.add(drift_press_activasRoutineBegin(snapshot));
      trial_train_ActivasLoopScheduler.add(drift_press_activasRoutineEachFrame());
      trial_train_ActivasLoopScheduler.add(drift_press_activasRoutineEnd());
      trial_train_ActivasLoopScheduler.add(ffix_trainactivasRoutineBegin(snapshot));
      trial_train_ActivasLoopScheduler.add(ffix_trainactivasRoutineEachFrame());
      trial_train_ActivasLoopScheduler.add(ffix_trainactivasRoutineEnd());
      const train_digitloop_ActivasLoopScheduler = new Scheduler(psychoJS);
      trial_train_ActivasLoopScheduler.add(train_digitloop_ActivasLoopBegin(train_digitloop_ActivasLoopScheduler, snapshot));
      trial_train_ActivasLoopScheduler.add(train_digitloop_ActivasLoopScheduler);
      trial_train_ActivasLoopScheduler.add(train_digitloop_ActivasLoopEnd);
      trial_train_ActivasLoopScheduler.add(recall_train_activasRoutineBegin(snapshot));
      trial_train_ActivasLoopScheduler.add(recall_train_activasRoutineEachFrame());
      trial_train_ActivasLoopScheduler.add(recall_train_activasRoutineEnd());
      trial_train_ActivasLoopScheduler.add(post_recall_train_activasRoutineBegin(snapshot));
      trial_train_ActivasLoopScheduler.add(post_recall_train_activasRoutineEachFrame());
      trial_train_ActivasLoopScheduler.add(post_recall_train_activasRoutineEnd());
      trial_train_ActivasLoopScheduler.add(endLoopIteration(trial_train_ActivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var train_digitloop_Activas;
function train_digitloop_ActivasLoopBegin(train_digitloop_ActivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    train_digitloop_Activas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan_train, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'train_digitloop_Activas'
    });
    psychoJS.experiment.addLoop(train_digitloop_Activas); // add the loop to the experiment
    currentLoop = train_digitloop_Activas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrain_digitloop_Activa of train_digitloop_Activas) {
      const snapshot = train_digitloop_Activas.getSnapshot();
      train_digitloop_ActivasLoopScheduler.add(importConditions(snapshot));
      train_digitloop_ActivasLoopScheduler.add(present_train_activasRoutineBegin(snapshot));
      train_digitloop_ActivasLoopScheduler.add(present_train_activasRoutineEachFrame());
      train_digitloop_ActivasLoopScheduler.add(present_train_activasRoutineEnd());
      train_digitloop_ActivasLoopScheduler.add(endLoopIteration(train_digitloop_ActivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function train_digitloop_ActivasLoopEnd() {
  psychoJS.experiment.removeLoop(train_digitloop_Activas);

  return Scheduler.Event.NEXT;
}


async function trial_train_ActivasLoopEnd() {
  psychoJS.experiment.removeLoop(trial_train_Activas);

  return Scheduler.Event.NEXT;
}


var trialActivas;
function trialActivasLoopBegin(trialActivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialActivas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: (("datasets/Dataset_" + ordenactivas[BlockActivas.thisN]) + ".xlsx"),
      seed: undefined, name: 'trialActivas'
    });
    psychoJS.experiment.addLoop(trialActivas); // add the loop to the experiment
    currentLoop = trialActivas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialActiva of trialActivas) {
      const snapshot = trialActivas.getSnapshot();
      trialActivasLoopScheduler.add(importConditions(snapshot));
      trialActivasLoopScheduler.add(drift_press_activasRoutineBegin(snapshot));
      trialActivasLoopScheduler.add(drift_press_activasRoutineEachFrame());
      trialActivasLoopScheduler.add(drift_press_activasRoutineEnd());
      trialActivasLoopScheduler.add(first_fixActivasRoutineBegin(snapshot));
      trialActivasLoopScheduler.add(first_fixActivasRoutineEachFrame());
      trialActivasLoopScheduler.add(first_fixActivasRoutineEnd());
      const digitLoop_ActivasLoopScheduler = new Scheduler(psychoJS);
      trialActivasLoopScheduler.add(digitLoop_ActivasLoopBegin(digitLoop_ActivasLoopScheduler, snapshot));
      trialActivasLoopScheduler.add(digitLoop_ActivasLoopScheduler);
      trialActivasLoopScheduler.add(digitLoop_ActivasLoopEnd);
      trialActivasLoopScheduler.add(RecallActivasRoutineBegin(snapshot));
      trialActivasLoopScheduler.add(RecallActivasRoutineEachFrame());
      trialActivasLoopScheduler.add(RecallActivasRoutineEnd());
      trialActivasLoopScheduler.add(post_recallActivasRoutineBegin(snapshot));
      trialActivasLoopScheduler.add(post_recallActivasRoutineEachFrame());
      trialActivasLoopScheduler.add(post_recallActivasRoutineEnd());
      trialActivasLoopScheduler.add(endLoopIteration(trialActivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var digitLoop_Activas;
function digitLoop_ActivasLoopBegin(digitLoop_ActivasLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    digitLoop_Activas = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'digitLoop_Activas'
    });
    psychoJS.experiment.addLoop(digitLoop_Activas); // add the loop to the experiment
    currentLoop = digitLoop_Activas;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisDigitLoop_Activa of digitLoop_Activas) {
      const snapshot = digitLoop_Activas.getSnapshot();
      digitLoop_ActivasLoopScheduler.add(importConditions(snapshot));
      digitLoop_ActivasLoopScheduler.add(PresentationActivasRoutineBegin(snapshot));
      digitLoop_ActivasLoopScheduler.add(PresentationActivasRoutineEachFrame());
      digitLoop_ActivasLoopScheduler.add(PresentationActivasRoutineEnd());
      digitLoop_ActivasLoopScheduler.add(endLoopIteration(digitLoop_ActivasLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function digitLoop_ActivasLoopEnd() {
  psychoJS.experiment.removeLoop(digitLoop_Activas);

  return Scheduler.Event.NEXT;
}


async function trialActivasLoopEnd() {
  psychoJS.experiment.removeLoop(trialActivas);

  return Scheduler.Event.NEXT;
}


async function BlockActivasLoopEnd() {
  psychoJS.experiment.removeLoop(BlockActivas);

  return Scheduler.Event.NEXT;
}


async function Block_OrderLoopEnd() {
  psychoJS.experiment.removeLoop(Block_Order);

  return Scheduler.Event.NEXT;
}


var _key_resp_2_allKeys;
var InstruccionesPasivaComponents;
function InstruccionesPasivaRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'InstruccionesPasiva'-------
    t = 0;
    InstruccionesPasivaClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image2.setImage(instrucciones_pasiva);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    InstruccionesPasivaComponents = [];
    InstruccionesPasivaComponents.push(image2);
    InstruccionesPasivaComponents.push(key_resp_2);
    
    for (const thisComponent of InstruccionesPasivaComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function InstruccionesPasivaRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'InstruccionesPasiva'-------
    // get current time
    t = InstruccionesPasivaClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image2* updates
    if (t >= 0.0 && image2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image2.tStart = t;  // (not accounting for frame time here)
      image2.frameNStart = frameN;  // exact frame index
      
      image2.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.25 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of InstruccionesPasivaComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstruccionesPasivaRoutineEnd() {
  return async function () {
    //------Ending Routine 'InstruccionesPasiva'-------
    for (const thisComponent of InstruccionesPasivaComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_2.stop();
    // the Routine "InstruccionesPasiva" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var firstfix_trainingComponents;
function firstfix_trainingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'firstfix_training'-------
    t = 0;
    firstfix_trainingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    start_trainPR.secs=0.5;
    start_trainPR.setVolume(1.0);
    firstfixtrain.setText('+');
    // keep track of which components have finished
    firstfix_trainingComponents = [];
    firstfix_trainingComponents.push(drift_trainPR);
    firstfix_trainingComponents.push(start_trainPR);
    firstfix_trainingComponents.push(firstfixtrain);
    
    for (const thisComponent of firstfix_trainingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function firstfix_trainingRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'firstfix_training'-------
    // get current time
    t = firstfix_trainingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *drift_trainPR* updates
    if (t >= 0.0 && drift_trainPR.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      drift_trainPR.tStart = t;  // (not accounting for frame time here)
      drift_trainPR.frameNStart = frameN;  // exact frame index
      
      drift_trainPR.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (drift_trainPR.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      drift_trainPR.setAutoDraw(false);
    }
    // start/stop start_trainPR
    if (t >= 0.0 && start_trainPR.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_trainPR.tStart = t;  // (not accounting for frame time here)
      start_trainPR.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ start_trainPR.play(); });  // screen flip
      start_trainPR.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (start_trainPR.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.5 > 0.5) {
        start_trainPR.stop();  // stop the sound (if longer than duration)
      }
      start_trainPR.status = PsychoJS.Status.FINISHED;
    }
    
    // *firstfixtrain* updates
    if (t >= 0.5 && firstfixtrain.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      firstfixtrain.tStart = t;  // (not accounting for frame time here)
      firstfixtrain.frameNStart = frameN;  // exact frame index
      
      firstfixtrain.setAutoDraw(true);
    }

    frameRemains = 0.5 + fixation_time_train - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (firstfixtrain.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      firstfixtrain.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of firstfix_trainingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function firstfix_trainingRoutineEnd() {
  return async function () {
    //------Ending Routine 'firstfix_training'-------
    for (const thisComponent of firstfix_trainingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    start_trainPR.stop();  // ensure sound has stopped at end of routine
    // the Routine "firstfix_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var presentation_trainingComponents;
function presentation_trainingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'presentation_training'-------
    t = 0;
    presentation_trainingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    digitpresentation_training.setText(digits_train.toString()[train_digitloopPasivas.thisN]);
    // keep track of which components have finished
    presentation_trainingComponents = [];
    presentation_trainingComponents.push(digitpresentation_training);
    
    for (const thisComponent of presentation_trainingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function presentation_trainingRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'presentation_training'-------
    // get current time
    t = presentation_trainingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *digitpresentation_training* updates
    if (t >= 0 && digitpresentation_training.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      digitpresentation_training.tStart = t;  // (not accounting for frame time here)
      digitpresentation_training.frameNStart = frameN;  // exact frame index
      
      digitpresentation_training.setAutoDraw(true);
    }

    frameRemains = 0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (digitpresentation_training.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      digitpresentation_training.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of presentation_trainingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function presentation_trainingRoutineEnd() {
  return async function () {
    //------Ending Routine 'presentation_training'-------
    for (const thisComponent of presentation_trainingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var answer_train_pasivas;
var recall_trainingComponents;
function recall_trainingRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'recall_training'-------
    t = 0;
    recall_trainingClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    answ_train.setText('');
    answ_train.refresh();
    answer_train_pasivas = Number.parseInt(answer_train);
    
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    recall_trainingComponents = [];
    recall_trainingComponents.push(recall_train);
    recall_trainingComponents.push(answ_train);
    
    for (const thisComponent of recall_trainingComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var correct;
var fbTxt;
function recall_trainingRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'recall_training'-------
    // get current time
    t = recall_trainingClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_train* updates
    if (t >= 0 && recall_train.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_train.tStart = t;  // (not accounting for frame time here)
      recall_train.frameNStart = frameN;  // exact frame index
      
      recall_train.setAutoDraw(true);
    }

    
    // *answ_train* updates
    if (t >= 0.0 && answ_train.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answ_train.tStart = t;  // (not accounting for frame time here)
      answ_train.frameNStart = frameN;  // exact frame index
      
      answ_train.setAutoDraw(true);
    }

    if (defaultKeyboard.getKeys({"keyList": ["return"]})) {
        answ_train.text = answ_train.text.rstrip();
        if ((answ_train.text === answer_train_pasivas.toString())) {
            correct = 1;
            fbTxt = "Correct!";
        } else {
            correct = 0;
            fbTxt = "Incorrect";
        }
        psychoJS.experiment.addData("correct", correct);
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of recall_trainingComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function recall_trainingRoutineEnd() {
  return async function () {
    //------Ending Routine 'recall_training'-------
    for (const thisComponent of recall_trainingComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('answ_train.text',answ_train.text)
    // the Routine "recall_training" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var post_recall_trainComponents;
function post_recall_trainRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'post_recall_train'-------
    t = 0;
    post_recall_trainClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    post_recall_trainComponents = [];
    post_recall_trainComponents.push(post_recall_training);
    
    for (const thisComponent of post_recall_trainComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function post_recall_trainRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'post_recall_train'-------
    // get current time
    t = post_recall_trainClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *post_recall_training* updates
    if (t >= 0.0 && post_recall_training.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      post_recall_training.tStart = t;  // (not accounting for frame time here)
      post_recall_training.frameNStart = frameN;  // exact frame index
      
      post_recall_training.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (post_recall_training.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      post_recall_training.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of post_recall_trainComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function post_recall_trainRoutineEnd() {
  return async function () {
    //------Ending Routine 'post_recall_train'-------
    for (const thisComponent of post_recall_trainComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_allKeys;
var start_trialComponents;
function start_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'start_trial'-------
    t = 0;
    start_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    start_trialComponents = [];
    start_trialComponents.push(end_training);
    start_trialComponents.push(key_resp);
    
    for (const thisComponent of start_trialComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function start_trialRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'start_trial'-------
    // get current time
    t = start_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_training* updates
    if (t >= 0.0 && end_training.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_training.tStart = t;  // (not accounting for frame time here)
      end_training.frameNStart = frameN;  // exact frame index
      
      end_training.setAutoDraw(true);
    }

    
    // *key_resp* updates
    if (t >= 0.5 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of start_trialComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var parar_el_trial;
function start_trialRoutineEnd() {
  return async function () {
    //------Ending Routine 'start_trial'-------
    for (const thisComponent of start_trialComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp.stop();
    parar_el_trial = false;
    
    // the Routine "start_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var first_fixationComponents;
function first_fixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'first_fixation'-------
    t = 0;
    first_fixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    startPR.secs=0.5;
    startPR.setVolume(1.0);
    first_fix_pas.setText('+');
    // keep track of which components have finished
    first_fixationComponents = [];
    first_fixationComponents.push(driftPR);
    first_fixationComponents.push(startPR);
    first_fixationComponents.push(first_fix_pas);
    
    for (const thisComponent of first_fixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function first_fixationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'first_fixation'-------
    // get current time
    t = first_fixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *driftPR* updates
    if (t >= 0.0 && driftPR.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      driftPR.tStart = t;  // (not accounting for frame time here)
      driftPR.frameNStart = frameN;  // exact frame index
      
      driftPR.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (driftPR.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      driftPR.setAutoDraw(false);
    }
    // start/stop startPR
    if (t >= 0.0 && startPR.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      startPR.tStart = t;  // (not accounting for frame time here)
      startPR.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ startPR.play(); });  // screen flip
      startPR.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (startPR.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.5 > 0.5) {
        startPR.stop();  // stop the sound (if longer than duration)
      }
      startPR.status = PsychoJS.Status.FINISHED;
    }
    
    // *first_fix_pas* updates
    if (t >= 0.5 && first_fix_pas.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_fix_pas.tStart = t;  // (not accounting for frame time here)
      first_fix_pas.frameNStart = frameN;  // exact frame index
      
      first_fix_pas.setAutoDraw(true);
    }

    frameRemains = 0.5 + fixation_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (first_fix_pas.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      first_fix_pas.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of first_fixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function first_fixationRoutineEnd() {
  return async function () {
    //------Ending Routine 'first_fixation'-------
    for (const thisComponent of first_fixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    startPR.stop();  // ensure sound has stopped at end of routine
    // the Routine "first_fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var Presentation_pasComponents;
function Presentation_pasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Presentation_pas'-------
    t = 0;
    Presentation_pasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    pres_text.setText(digits.toString()[digitLoop_Pasivas.thisN]);
    // keep track of which components have finished
    Presentation_pasComponents = [];
    Presentation_pasComponents.push(pres_text);
    
    for (const thisComponent of Presentation_pasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Presentation_pasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Presentation_pas'-------
    // get current time
    t = Presentation_pasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pres_text* updates
    if (t >= 0 && pres_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pres_text.tStart = t;  // (not accounting for frame time here)
      pres_text.frameNStart = frameN;  // exact frame index
      
      pres_text.setAutoDraw(true);
    }

    frameRemains = 0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pres_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pres_text.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Presentation_pasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Presentation_pasRoutineEnd() {
  return async function () {
    //------Ending Routine 'Presentation_pas'-------
    for (const thisComponent of Presentation_pasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var answer_Pasive;
var Recall_pasivasComponents;
function Recall_pasivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Recall_pasivas'-------
    t = 0;
    Recall_pasivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    answer_box.setText('');
    answer_box.refresh();
    answer_Pasive = Number.parseInt(answer);
    
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    Recall_pasivasComponents = [];
    Recall_pasivasComponents.push(recall_txt);
    Recall_pasivasComponents.push(answer_box);
    
    for (const thisComponent of Recall_pasivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Recall_pasivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Recall_pasivas'-------
    // get current time
    t = Recall_pasivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txt* updates
    if (t >= 0 && recall_txt.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txt.tStart = t;  // (not accounting for frame time here)
      recall_txt.frameNStart = frameN;  // exact frame index
      
      recall_txt.setAutoDraw(true);
    }

    
    // *answer_box* updates
    if (t >= 0.0 && answer_box.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer_box.tStart = t;  // (not accounting for frame time here)
      answer_box.frameNStart = frameN;  // exact frame index
      
      answer_box.setAutoDraw(true);
    }

    if (defaultKeyboard.getKeys({"keyList": ["return"]})) {
        answer_box.text = answer_box.text.rstrip();
        if ((answer_box.text === answer_Pasive.toString())) {
            correct = 1;
        } else {
            correct = 0;
        }
        psychoJS.experiment.addData("correct", correct);
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Recall_pasivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Recall_pasivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'Recall_pasivas'-------
    for (const thisComponent of Recall_pasivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('answer_box.text',answer_box.text)
    if (((trial_Pasiva.thisTrialN === 0) || (trial_Pasiva.thisTrialN === 1))) {
        if ((correct === 1)) {
            previous_count += 1;
            console.log(` trial = ${trial_Pasiva.thisTrialN} previous_count = ${previous_count}`);
        }
    } else {
        if (((trial_Pasiva.thisTrialN === 2) || (trial_Pasiva.thisTrialN === 3))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_Pasiva.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_Pasiva.thisTrialN === 3)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`trial = ${trial_Pasiva.thisTrialN} parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_Pasiva.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_Pasiva.thisTrialN === 4) || (trial_Pasiva.thisTrialN === 5))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_Pasiva.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_Pasiva.thisTrialN === 5)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_Pasiva.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_Pasiva.thisTrialN === 6) || (trial_Pasiva.thisTrialN === 7))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_Pasiva.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_Pasiva.thisTrialN === 7)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_Pasiva.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_Pasiva.thisTrialN === 8) || (trial_Pasiva.thisTrialN === 9))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_Pasiva.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_Pasiva.thisTrialN === 9)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_Pasiva.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_Pasiva.thisTrialN === 10) || (trial_Pasiva.thisTrialN === 11))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_Pasiva.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_Pasiva.thisTrialN === 11)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_Pasiva.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_Pasiva.thisTrialN === 12) || (trial_Pasiva.thisTrialN === 13))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_Pasiva.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_Pasiva.thisTrialN === 13)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_Pasiva.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    }
    
    // the Routine "Recall_pasivas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var post_recallPasivaComponents;
function post_recallPasivaRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'post_recallPasiva'-------
    t = 0;
    post_recallPasivaClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    post_recallPasivaComponents = [];
    post_recallPasivaComponents.push(postrecallPR);
    
    for (const thisComponent of post_recallPasivaComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function post_recallPasivaRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'post_recallPasiva'-------
    // get current time
    t = post_recallPasivaClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *postrecallPR* updates
    if (t >= 0.0 && postrecallPR.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postrecallPR.tStart = t;  // (not accounting for frame time here)
      postrecallPR.frameNStart = frameN;  // exact frame index
      
      postrecallPR.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postrecallPR.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postrecallPR.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of post_recallPasivaComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function post_recallPasivaRoutineEnd() {
  return async function () {
    //------Ending Routine 'post_recallPasiva'-------
    for (const thisComponent of post_recallPasivaComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (parar_el_trial) {
        trial_Pasiva.finished = true;
    }
    
    return Scheduler.Event.NEXT;
  };
}


var LickertPasivasComponents;
function LickertPasivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LickertPasivas'-------
    t = 0;
    LickertPasivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    dif_licker.reset()
    // keep track of which components have finished
    LickertPasivasComponents = [];
    LickertPasivasComponents.push(Dificultad_pasivas);
    LickertPasivasComponents.push(dif_licker);
    
    for (const thisComponent of LickertPasivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function LickertPasivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LickertPasivas'-------
    // get current time
    t = LickertPasivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Dificultad_pasivas* updates
    if (t >= 0.0 && Dificultad_pasivas.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Dificultad_pasivas.tStart = t;  // (not accounting for frame time here)
      Dificultad_pasivas.frameNStart = frameN;  // exact frame index
      
      Dificultad_pasivas.setAutoDraw(true);
    }

    
    // *dif_licker* updates
    if (t >= 0.0 && dif_licker.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dif_licker.tStart = t;  // (not accounting for frame time here)
      dif_licker.frameNStart = frameN;  // exact frame index
      
      dif_licker.setAutoDraw(true);
    }

    
    // Check dif_licker for response to end routine
    if (dif_licker.getRating() !== undefined && dif_licker.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of LickertPasivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LickertPasivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'LickertPasivas'-------
    for (const thisComponent of LickertPasivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('dif_licker.response', dif_licker.getRating());
    psychoJS.experiment.addData('dif_licker.rt', dif_licker.getRT());
    // the Routine "LickertPasivas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_6_allKeys;
var EndTaskComponents;
function EndTaskRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'EndTask'-------
    t = 0;
    EndTaskClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    siguiente_tarea.setText('Esta tarea terminó. \n* Presiona la barra para continuar con la siguiente*');
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    // keep track of which components have finished
    EndTaskComponents = [];
    EndTaskComponents.push(siguiente_tarea);
    EndTaskComponents.push(key_resp_6);
    
    for (const thisComponent of EndTaskComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function EndTaskRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'EndTask'-------
    // get current time
    t = EndTaskClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *siguiente_tarea* updates
    if (t >= 0.0 && siguiente_tarea.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      siguiente_tarea.tStart = t;  // (not accounting for frame time here)
      siguiente_tarea.frameNStart = frameN;  // exact frame index
      
      siguiente_tarea.setAutoDraw(true);
    }

    
    // *key_resp_6* updates
    if (t >= 0.25 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.clearEvents(); });
    }

    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].name;  // just the last key pressed
        key_resp_6.rt = _key_resp_6_allKeys[_key_resp_6_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of EndTaskComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndTaskRoutineEnd() {
  return async function () {
    //------Ending Routine 'EndTask'-------
    for (const thisComponent of EndTaskComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        routineTimer.reset();
        }
    
    key_resp_6.stop();
    // the Routine "EndTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_3_allKeys;
var Instr_ActivasComponents;
function Instr_ActivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Instr_Activas'-------
    t = 0;
    Instr_ActivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image2_2.setImage(instrucciones_activa);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    // keep track of which components have finished
    Instr_ActivasComponents = [];
    Instr_ActivasComponents.push(image2_2);
    Instr_ActivasComponents.push(key_resp_3);
    
    for (const thisComponent of Instr_ActivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Instr_ActivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Instr_Activas'-------
    // get current time
    t = Instr_ActivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image2_2* updates
    if (t >= 0.0 && image2_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image2_2.tStart = t;  // (not accounting for frame time here)
      image2_2.frameNStart = frameN;  // exact frame index
      
      image2_2.setAutoDraw(true);
    }

    
    // *key_resp_3* updates
    if (t >= 0.25 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
    }

    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].name;  // just the last key pressed
        key_resp_3.rt = _key_resp_3_allKeys[_key_resp_3_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of Instr_ActivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Instr_ActivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'Instr_Activas'-------
    for (const thisComponent of Instr_ActivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_3.stop();
    // the Routine "Instr_Activas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_5_allKeys;
var drift_press_activasComponents;
function drift_press_activasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'drift_press_activas'-------
    t = 0;
    drift_press_activasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    start_trainPR_2.secs=0.5;
    start_trainPR_2.setVolume(1.0);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    // keep track of which components have finished
    drift_press_activasComponents = [];
    drift_press_activasComponents.push(start_trainPR_2);
    drift_press_activasComponents.push(drift_trainPR_2);
    drift_press_activasComponents.push(firstfix_activas);
    drift_press_activasComponents.push(key_resp_5);
    
    for (const thisComponent of drift_press_activasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function drift_press_activasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'drift_press_activas'-------
    // get current time
    t = drift_press_activasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // start/stop start_trainPR_2
    if (t >= 0.0 && start_trainPR_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      start_trainPR_2.tStart = t;  // (not accounting for frame time here)
      start_trainPR_2.frameNStart = frameN;  // exact frame index
      
      psychoJS.window.callOnFlip(function(){ start_trainPR_2.play(); });  // screen flip
      start_trainPR_2.status = PsychoJS.Status.STARTED;
    }
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (start_trainPR_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      if (0.5 > 0.5) {
        start_trainPR_2.stop();  // stop the sound (if longer than duration)
      }
      start_trainPR_2.status = PsychoJS.Status.FINISHED;
    }
    
    // *drift_trainPR_2* updates
    if (t >= 0.0 && drift_trainPR_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      drift_trainPR_2.tStart = t;  // (not accounting for frame time here)
      drift_trainPR_2.frameNStart = frameN;  // exact frame index
      
      drift_trainPR_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (drift_trainPR_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      drift_trainPR_2.setAutoDraw(false);
    }
    
    // *firstfix_activas* updates
    if (t >= 0.5 && firstfix_activas.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      firstfix_activas.tStart = t;  // (not accounting for frame time here)
      firstfix_activas.frameNStart = frameN;  // exact frame index
      
      firstfix_activas.setAutoDraw(true);
    }

    
    // *key_resp_5* updates
    if (t >= 0.5 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.clearEvents(); });
    }

    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].name;  // just the last key pressed
        key_resp_5.rt = _key_resp_5_allKeys[_key_resp_5_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of drift_press_activasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function drift_press_activasRoutineEnd() {
  return async function () {
    //------Ending Routine 'drift_press_activas'-------
    for (const thisComponent of drift_press_activasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    start_trainPR_2.stop();  // ensure sound has stopped at end of routine
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        routineTimer.reset();
        }
    
    key_resp_5.stop();
    // the Routine "drift_press_activas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var ffix_trainactivasComponents;
function ffix_trainactivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'ffix_trainactivas'-------
    t = 0;
    ffix_trainactivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    firsfixtrain_activa.setText('+');
    // keep track of which components have finished
    ffix_trainactivasComponents = [];
    ffix_trainactivasComponents.push(firsfixtrain_activa);
    
    for (const thisComponent of ffix_trainactivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ffix_trainactivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'ffix_trainactivas'-------
    // get current time
    t = ffix_trainactivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *firsfixtrain_activa* updates
    if (t >= 0.0 && firsfixtrain_activa.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      firsfixtrain_activa.tStart = t;  // (not accounting for frame time here)
      firsfixtrain_activa.frameNStart = frameN;  // exact frame index
      
      firsfixtrain_activa.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixation_time_train - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (firsfixtrain_activa.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      firsfixtrain_activa.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of ffix_trainactivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ffix_trainactivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'ffix_trainactivas'-------
    for (const thisComponent of ffix_trainactivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "ffix_trainactivas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var present_train_activasComponents;
function present_train_activasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'present_train_activas'-------
    t = 0;
    present_train_activasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    digitpresentation_training_2.setText(digits_train.toString()[train_digitloop_Activas.thisN]);
    // keep track of which components have finished
    present_train_activasComponents = [];
    present_train_activasComponents.push(digitpresentation_training_2);
    
    for (const thisComponent of present_train_activasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function present_train_activasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'present_train_activas'-------
    // get current time
    t = present_train_activasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *digitpresentation_training_2* updates
    if (t >= 0 && digitpresentation_training_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      digitpresentation_training_2.tStart = t;  // (not accounting for frame time here)
      digitpresentation_training_2.frameNStart = frameN;  // exact frame index
      
      digitpresentation_training_2.setAutoDraw(true);
    }

    frameRemains = 0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (digitpresentation_training_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      digitpresentation_training_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of present_train_activasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function present_train_activasRoutineEnd() {
  return async function () {
    //------Ending Routine 'present_train_activas'-------
    for (const thisComponent of present_train_activasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var answer_train_activas;
var recall_train_activasComponents;
function recall_train_activasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'recall_train_activas'-------
    t = 0;
    recall_train_activasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    answ_train_2.setText('');
    answ_train_2.refresh();
    answer_train_activas = Number.parseInt(answer_train);
    
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    recall_train_activasComponents = [];
    recall_train_activasComponents.push(recall_train_2);
    recall_train_activasComponents.push(answ_train_2);
    
    for (const thisComponent of recall_train_activasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function recall_train_activasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'recall_train_activas'-------
    // get current time
    t = recall_train_activasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_train_2* updates
    if (t >= 0 && recall_train_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_train_2.tStart = t;  // (not accounting for frame time here)
      recall_train_2.frameNStart = frameN;  // exact frame index
      
      recall_train_2.setAutoDraw(true);
    }

    
    // *answ_train_2* updates
    if (t >= 0.0 && answ_train_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answ_train_2.tStart = t;  // (not accounting for frame time here)
      answ_train_2.frameNStart = frameN;  // exact frame index
      
      answ_train_2.setAutoDraw(true);
    }

    if (defaultKeyboard.getKeys({"keyList": ["return"]})) {
        answ_train_2.text = answ_train_2.text.rstrip();
        if ((answ_train_2.text === answer_train_activas.toString())) {
            correct = 1;
            fbTxt = "Correct!";
        } else {
            correct = 0;
            fbTxt = "Incorrect";
        }
        psychoJS.experiment.addData("correct", correct);
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of recall_train_activasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function recall_train_activasRoutineEnd() {
  return async function () {
    //------Ending Routine 'recall_train_activas'-------
    for (const thisComponent of recall_train_activasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('answ_train_2.text',answ_train_2.text)
    // the Routine "recall_train_activas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var post_recall_train_activasComponents;
function post_recall_train_activasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'post_recall_train_activas'-------
    t = 0;
    post_recall_train_activasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    post_recall_train_activasComponents = [];
    post_recall_train_activasComponents.push(post_recall_training_2);
    
    for (const thisComponent of post_recall_train_activasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function post_recall_train_activasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'post_recall_train_activas'-------
    // get current time
    t = post_recall_train_activasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *post_recall_training_2* updates
    if (t >= 0.0 && post_recall_training_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      post_recall_training_2.tStart = t;  // (not accounting for frame time here)
      post_recall_training_2.frameNStart = frameN;  // exact frame index
      
      post_recall_training_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (post_recall_training_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      post_recall_training_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of post_recall_train_activasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function post_recall_train_activasRoutineEnd() {
  return async function () {
    //------Ending Routine 'post_recall_train_activas'-------
    for (const thisComponent of post_recall_train_activasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_4_allKeys;
var start_trialActivasComponents;
function start_trialActivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'start_trialActivas'-------
    t = 0;
    start_trialActivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    // keep track of which components have finished
    start_trialActivasComponents = [];
    start_trialActivasComponents.push(end_training_2);
    start_trialActivasComponents.push(key_resp_4);
    
    for (const thisComponent of start_trialActivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function start_trialActivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'start_trialActivas'-------
    // get current time
    t = start_trialActivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *end_training_2* updates
    if (t >= 0.0 && end_training_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      end_training_2.tStart = t;  // (not accounting for frame time here)
      end_training_2.frameNStart = frameN;  // exact frame index
      
      end_training_2.setAutoDraw(true);
    }

    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.clearEvents(); });
    }

    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].name;  // just the last key pressed
        key_resp_4.rt = _key_resp_4_allKeys[_key_resp_4_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of start_trialActivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function start_trialActivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'start_trialActivas'-------
    for (const thisComponent of start_trialActivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    key_resp_4.stop();
    parar_el_trial = false;
    previous_count = 0;
    current_count = 0;
    
    // the Routine "start_trialActivas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var first_fixActivasComponents;
function first_fixActivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'first_fixActivas'-------
    t = 0;
    first_fixActivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    first_fix_active.setText('+');
    // keep track of which components have finished
    first_fixActivasComponents = [];
    first_fixActivasComponents.push(first_fix_active);
    
    for (const thisComponent of first_fixActivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function first_fixActivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'first_fixActivas'-------
    // get current time
    t = first_fixActivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *first_fix_active* updates
    if (t >= 0.0 && first_fix_active.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_fix_active.tStart = t;  // (not accounting for frame time here)
      first_fix_active.frameNStart = frameN;  // exact frame index
      
      first_fix_active.setAutoDraw(true);
    }

    frameRemains = 0.0 + fixation_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (first_fix_active.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      first_fix_active.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of first_fixActivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function first_fixActivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'first_fixActivas'-------
    for (const thisComponent of first_fixActivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "first_fixActivas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var PresentationActivasComponents;
function PresentationActivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'PresentationActivas'-------
    t = 0;
    PresentationActivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    pres_text_active.setText(digits.toString()[digitLoop_Activas.thisN]);
    // keep track of which components have finished
    PresentationActivasComponents = [];
    PresentationActivasComponents.push(pres_text_active);
    
    for (const thisComponent of PresentationActivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function PresentationActivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'PresentationActivas'-------
    // get current time
    t = PresentationActivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *pres_text_active* updates
    if (t >= 0 && pres_text_active.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      pres_text_active.tStart = t;  // (not accounting for frame time here)
      pres_text_active.frameNStart = frameN;  // exact frame index
      
      pres_text_active.setAutoDraw(true);
    }

    frameRemains = 0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (pres_text_active.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      pres_text_active.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of PresentationActivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PresentationActivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'PresentationActivas'-------
    for (const thisComponent of PresentationActivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


var answer_active;
var RecallActivasComponents;
function RecallActivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'RecallActivas'-------
    t = 0;
    RecallActivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    answer_box_2.setText('');
    answer_box_2.refresh();
    answer_active = Number.parseInt(answer);
    
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    RecallActivasComponents = [];
    RecallActivasComponents.push(recall_txt_2);
    RecallActivasComponents.push(answer_box_2);
    
    for (const thisComponent of RecallActivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function RecallActivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'RecallActivas'-------
    // get current time
    t = RecallActivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *recall_txt_2* updates
    if (t >= 0 && recall_txt_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      recall_txt_2.tStart = t;  // (not accounting for frame time here)
      recall_txt_2.frameNStart = frameN;  // exact frame index
      
      recall_txt_2.setAutoDraw(true);
    }

    
    // *answer_box_2* updates
    if (t >= 0.0 && answer_box_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      answer_box_2.tStart = t;  // (not accounting for frame time here)
      answer_box_2.frameNStart = frameN;  // exact frame index
      
      answer_box_2.setAutoDraw(true);
    }

    if (defaultKeyboard.getKeys({"keyList": ["return"]})) {
        answer_box_2.text = answer_box_2.text.rstrip();
        if ((answer_box_2.text === answer_active.toString())) {
            correct = 1;
        } else {
            correct = 0;
        }
        psychoJS.experiment.addData("correct", correct);
        continueRoutine = false;
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of RecallActivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RecallActivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'RecallActivas'-------
    for (const thisComponent of RecallActivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('answer_box_2.text',answer_box_2.text)
    if (((trialActivas.thisTrialN === 0) || (trialActivas.thisTrialN === 1))) {
        if ((correct === 1)) {
            previous_count += 1;
            console.log(` trial = ${trialActivas.thisTrialN} previous_count = ${previous_count}`);
        }
    } else {
        if (((trialActivas.thisTrialN === 2) || (trialActivas.thisTrialN === 3))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trialActivas.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trialActivas.thisTrialN === 3)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`trial = ${trialActivas.thisTrialN} parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trialActivas.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trialActivas.thisTrialN === 4) || (trialActivas.thisTrialN === 5))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trialActivas.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trialActivas.thisTrialN === 5)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trialActivas.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trialActivas.thisTrialN === 6) || (trialActivas.thisTrialN === 7))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trialActivas.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trialActivas.thisTrialN === 7)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trialActivas.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trialActivas.thisTrialN === 8) || (trialActivas.thisTrialN === 9))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trialActivas.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trialActivas.thisTrialN === 9)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trialActivas.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trialActivas.thisTrialN === 10) || (trialActivas.thisTrialN === 11))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trialActivas.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trialActivas.thisTrialN === 11)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trialActivas.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trialActivas.thisTrialN === 12) || (trialActivas.thisTrialN === 13))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trialActivas.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trialActivas.thisTrialN === 13)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trialActivas.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    }
    
    // the Routine "RecallActivas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var post_recallActivasComponents;
function post_recallActivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'post_recallActivas'-------
    t = 0;
    post_recallActivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    post_recallActivasComponents = [];
    post_recallActivasComponents.push(postrecallPR_2);
    
    for (const thisComponent of post_recallActivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function post_recallActivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'post_recallActivas'-------
    // get current time
    t = post_recallActivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *postrecallPR_2* updates
    if (t >= 0.0 && postrecallPR_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      postrecallPR_2.tStart = t;  // (not accounting for frame time here)
      postrecallPR_2.frameNStart = frameN;  // exact frame index
      
      postrecallPR_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (postrecallPR_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      postrecallPR_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of post_recallActivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function post_recallActivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'post_recallActivas'-------
    for (const thisComponent of post_recallActivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    if (parar_el_trial) {
        trialActivas.finished = true;
    }
    
    return Scheduler.Event.NEXT;
  };
}


var LickertActivasComponents;
function LickertActivasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'LickertActivas'-------
    t = 0;
    LickertActivasClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    dif_licker_2.reset()
    // keep track of which components have finished
    LickertActivasComponents = [];
    LickertActivasComponents.push(Dificultad_activas);
    LickertActivasComponents.push(dif_licker_2);
    
    for (const thisComponent of LickertActivasComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function LickertActivasRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'LickertActivas'-------
    // get current time
    t = LickertActivasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Dificultad_activas* updates
    if (t >= 0.0 && Dificultad_activas.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Dificultad_activas.tStart = t;  // (not accounting for frame time here)
      Dificultad_activas.frameNStart = frameN;  // exact frame index
      
      Dificultad_activas.setAutoDraw(true);
    }

    
    // *dif_licker_2* updates
    if (t >= 0.0 && dif_licker_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dif_licker_2.tStart = t;  // (not accounting for frame time here)
      dif_licker_2.frameNStart = frameN;  // exact frame index
      
      dif_licker_2.setAutoDraw(true);
    }

    
    // Check dif_licker_2 for response to end routine
    if (dif_licker_2.getRating() !== undefined && dif_licker_2.status === PsychoJS.Status.STARTED) {
      continueRoutine = false; }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of LickertActivasComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LickertActivasRoutineEnd() {
  return async function () {
    //------Ending Routine 'LickertActivas'-------
    for (const thisComponent of LickertActivasComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('dif_licker_2.response', dif_licker_2.getRating());
    psychoJS.experiment.addData('dif_licker_2.rt', dif_licker_2.getRT());
    // the Routine "LickertActivas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var FinalComponents;
function FinalRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Final'-------
    t = 0;
    FinalClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.500000);
    // update component parameters for each repeat
    // keep track of which components have finished
    FinalComponents = [];
    FinalComponents.push(text_2);
    
    for (const thisComponent of FinalComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FinalRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Final'-------
    // get current time
    t = FinalClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    for (const thisComponent of FinalComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FinalRoutineEnd() {
  return async function () {
    //------Ending Routine 'Final'-------
    for (const thisComponent of FinalComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
