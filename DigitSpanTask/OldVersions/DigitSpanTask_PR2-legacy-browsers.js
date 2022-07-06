/************************** 
 * Digitspantask_Pr2 Test *
 **************************/


// store info about the experiment session:
let expName = 'DigitSpanTask_PR2';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
const instrucloop_PRLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(instrucloop_PRLoopBegin(instrucloop_PRLoopScheduler));
flowScheduler.add(instrucloop_PRLoopScheduler);
flowScheduler.add(instrucloop_PRLoopEnd);
const trial_trainingPRLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trial_trainingPRLoopBegin(trial_trainingPRLoopScheduler));
flowScheduler.add(trial_trainingPRLoopScheduler);
flowScheduler.add(trial_trainingPRLoopEnd);
flowScheduler.add(start_trialRoutineBegin());
flowScheduler.add(start_trialRoutineEachFrame());
flowScheduler.add(start_trialRoutineEnd());
const trial_PRLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trial_PRLoopBegin(trial_PRLoopScheduler));
flowScheduler.add(trial_PRLoopScheduler);
flowScheduler.add(trial_PRLoopEnd);
flowScheduler.add(LickertRoutineBegin());
flowScheduler.add(LickertRoutineEachFrame());
flowScheduler.add(LickertRoutineEnd());
flowScheduler.add(EndRoutineBegin());
flowScheduler.add(EndRoutineEachFrame());
flowScheduler.add(EndRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'datasets/instructions.xlsx', 'path': 'datasets/instructions.xlsx'},
    {'name': 'datasets/instruccion1_pasiva.png', 'path': 'datasets/instruccion1_pasiva.png'},
    {'name': 'datasets/Bienvenida.png', 'path': 'datasets/Bienvenida.png'},
    {'name': 'datasets/trial_init.wav', 'path': 'datasets/trial_init.wav'},
    {'name': 'datasets/training_pr.xlsx', 'path': 'datasets/training_pr.xlsx'},
    {'name': 'datasets/instruccion1_activa.png', 'path': 'datasets/instruccion1_activa.png'},
    {'name': 'datasets/instruccion3.png', 'path': 'datasets/instruccion3.png'},
    {'name': 'datasets/drift.png', 'path': 'datasets/drift.png'},
    {'name': 'datasets/finpractica.png', 'path': 'datasets/finpractica.png'},
    {'name': 'datasets/Dataset_PR.xlsx', 'path': 'datasets/Dataset_PR.xlsx'},
    {'name': 'datasets/instruccion2.png', 'path': 'datasets/instruccion2.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
async function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.1.3';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

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
var Bienvenida_text;
var key_bienvenida;
var Bienvenida_img;
var InstruccionesClock;
var image;
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
var first_fix;
var PresentationClock;
var pres_text;
var RecallClock;
var recall_txt;
var answer_box;
var post_recallPRClock;
var postrecallPR;
var LickertClock;
var Dificultad;
var dif_licker;
var EndClock;
var thank_you;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "Bienvenida"
  BienvenidaClock = new util.Clock();
  Bienvenida_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'Bienvenida_text',
    text: '¡Bienvenid@!\n\nGracias por participar en nuestro estudio.\n\nPresiona "barra espaciadora" para ver las instrucciones',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  key_bienvenida = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Bienvenida_img = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Bienvenida_img', units : undefined, 
    image : 'datasets/Bienvenida.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : undefined,
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  // Initialize components for Routine "Instrucciones"
  InstruccionesClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : undefined, 
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
  first_fix = new visual.TextStim({
    win: psychoJS.window,
    name: 'first_fix',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  // Initialize components for Routine "Presentation"
  PresentationClock = new util.Clock();
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
  
  // Initialize components for Routine "Recall"
  RecallClock = new util.Clock();
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
  
  // Initialize components for Routine "post_recallPR"
  post_recallPRClock = new util.Clock();
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
  
  // Initialize components for Routine "Lickert"
  LickertClock = new util.Clock();
  Dificultad = new visual.TextStim({
    win: psychoJS.window,
    name: 'Dificultad',
    text: '¿Cuán difícil encontraste la tarea en general?',
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
  
  // Initialize components for Routine "End"
  EndClock = new util.Clock();
  thank_you = new visual.TextStim({
    win: psychoJS.window,
    name: 'thank_you',
    text: 'El experimento terminó.\n¡Gracias por participar!',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
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
    BienvenidaComponents.push(Bienvenida_text);
    BienvenidaComponents.push(key_bienvenida);
    BienvenidaComponents.push(Bienvenida_img);
    
    BienvenidaComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *Bienvenida_text* updates
    if (t >= 0.0 && Bienvenida_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Bienvenida_text.tStart = t;  // (not accounting for frame time here)
      Bienvenida_text.frameNStart = frameN;  // exact frame index
      
      Bienvenida_text.setAutoDraw(true);
    }

    
    // *key_bienvenida* updates
    if (t >= 0.0 && key_bienvenida.status === PsychoJS.Status.NOT_STARTED) {
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
    BienvenidaComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    BienvenidaComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_bienvenida.stop();
    // the Routine "Bienvenida" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var instrucloop_PR;
var currentLoop;
function instrucloop_PRLoopBegin(instrucloop_PRLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    instrucloop_PR = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'datasets/instructions.xlsx',
      seed: undefined, name: 'instrucloop_PR'
    });
    psychoJS.experiment.addLoop(instrucloop_PR); // add the loop to the experiment
    currentLoop = instrucloop_PR;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    instrucloop_PR.forEach(function() {
      const snapshot = instrucloop_PR.getSnapshot();
    
      instrucloop_PRLoopScheduler.add(importConditions(snapshot));
      instrucloop_PRLoopScheduler.add(InstruccionesRoutineBegin(snapshot));
      instrucloop_PRLoopScheduler.add(InstruccionesRoutineEachFrame());
      instrucloop_PRLoopScheduler.add(InstruccionesRoutineEnd());
      instrucloop_PRLoopScheduler.add(endLoopIteration(instrucloop_PRLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function instrucloop_PRLoopEnd() {
  psychoJS.experiment.removeLoop(instrucloop_PR);

  return Scheduler.Event.NEXT;
}


var trial_trainingPR;
function trial_trainingPRLoopBegin(trial_trainingPRLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trial_trainingPR = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'datasets/training_pr.xlsx',
      seed: undefined, name: 'trial_trainingPR'
    });
    psychoJS.experiment.addLoop(trial_trainingPR); // add the loop to the experiment
    currentLoop = trial_trainingPR;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trial_trainingPR.forEach(function() {
      const snapshot = trial_trainingPR.getSnapshot();
    
      trial_trainingPRLoopScheduler.add(importConditions(snapshot));
      trial_trainingPRLoopScheduler.add(firstfix_trainingRoutineBegin(snapshot));
      trial_trainingPRLoopScheduler.add(firstfix_trainingRoutineEachFrame());
      trial_trainingPRLoopScheduler.add(firstfix_trainingRoutineEnd());
      const train_digitloopPRLoopScheduler = new Scheduler(psychoJS);
      trial_trainingPRLoopScheduler.add(train_digitloopPRLoopBegin(train_digitloopPRLoopScheduler, snapshot));
      trial_trainingPRLoopScheduler.add(train_digitloopPRLoopScheduler);
      trial_trainingPRLoopScheduler.add(train_digitloopPRLoopEnd);
      trial_trainingPRLoopScheduler.add(recall_trainingRoutineBegin(snapshot));
      trial_trainingPRLoopScheduler.add(recall_trainingRoutineEachFrame());
      trial_trainingPRLoopScheduler.add(recall_trainingRoutineEnd());
      trial_trainingPRLoopScheduler.add(post_recall_trainRoutineBegin(snapshot));
      trial_trainingPRLoopScheduler.add(post_recall_trainRoutineEachFrame());
      trial_trainingPRLoopScheduler.add(post_recall_trainRoutineEnd());
      trial_trainingPRLoopScheduler.add(endLoopIteration(trial_trainingPRLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var train_digitloopPR;
function train_digitloopPRLoopBegin(train_digitloopPRLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    train_digitloopPR = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan_train, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'train_digitloopPR'
    });
    psychoJS.experiment.addLoop(train_digitloopPR); // add the loop to the experiment
    currentLoop = train_digitloopPR;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    train_digitloopPR.forEach(function() {
      const snapshot = train_digitloopPR.getSnapshot();
    
      train_digitloopPRLoopScheduler.add(importConditions(snapshot));
      train_digitloopPRLoopScheduler.add(presentation_trainingRoutineBegin(snapshot));
      train_digitloopPRLoopScheduler.add(presentation_trainingRoutineEachFrame());
      train_digitloopPRLoopScheduler.add(presentation_trainingRoutineEnd());
      train_digitloopPRLoopScheduler.add(endLoopIteration(train_digitloopPRLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function train_digitloopPRLoopEnd() {
  psychoJS.experiment.removeLoop(train_digitloopPR);

  return Scheduler.Event.NEXT;
}


async function trial_trainingPRLoopEnd() {
  psychoJS.experiment.removeLoop(trial_trainingPR);

  return Scheduler.Event.NEXT;
}


var trial_PR;
function trial_PRLoopBegin(trial_PRLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trial_PR = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'datasets/Dataset_PR.xlsx',
      seed: undefined, name: 'trial_PR'
    });
    psychoJS.experiment.addLoop(trial_PR); // add the loop to the experiment
    currentLoop = trial_PR;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trial_PR.forEach(function() {
      const snapshot = trial_PR.getSnapshot();
    
      trial_PRLoopScheduler.add(importConditions(snapshot));
      trial_PRLoopScheduler.add(first_fixationRoutineBegin(snapshot));
      trial_PRLoopScheduler.add(first_fixationRoutineEachFrame());
      trial_PRLoopScheduler.add(first_fixationRoutineEnd());
      const digitLoop_PRLoopScheduler = new Scheduler(psychoJS);
      trial_PRLoopScheduler.add(digitLoop_PRLoopBegin(digitLoop_PRLoopScheduler, snapshot));
      trial_PRLoopScheduler.add(digitLoop_PRLoopScheduler);
      trial_PRLoopScheduler.add(digitLoop_PRLoopEnd);
      trial_PRLoopScheduler.add(RecallRoutineBegin(snapshot));
      trial_PRLoopScheduler.add(RecallRoutineEachFrame());
      trial_PRLoopScheduler.add(RecallRoutineEnd());
      trial_PRLoopScheduler.add(post_recallPRRoutineBegin(snapshot));
      trial_PRLoopScheduler.add(post_recallPRRoutineEachFrame());
      trial_PRLoopScheduler.add(post_recallPRRoutineEnd());
      trial_PRLoopScheduler.add(endLoopIteration(trial_PRLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var digitLoop_PR;
function digitLoop_PRLoopBegin(digitLoop_PRLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    digitLoop_PR = new TrialHandler({
      psychoJS: psychoJS,
      nReps: digitSpan, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'digitLoop_PR'
    });
    psychoJS.experiment.addLoop(digitLoop_PR); // add the loop to the experiment
    currentLoop = digitLoop_PR;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    digitLoop_PR.forEach(function() {
      const snapshot = digitLoop_PR.getSnapshot();
    
      digitLoop_PRLoopScheduler.add(importConditions(snapshot));
      digitLoop_PRLoopScheduler.add(PresentationRoutineBegin(snapshot));
      digitLoop_PRLoopScheduler.add(PresentationRoutineEachFrame());
      digitLoop_PRLoopScheduler.add(PresentationRoutineEnd());
      digitLoop_PRLoopScheduler.add(endLoopIteration(digitLoop_PRLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function digitLoop_PRLoopEnd() {
  psychoJS.experiment.removeLoop(digitLoop_PR);

  return Scheduler.Event.NEXT;
}


async function trial_PRLoopEnd() {
  psychoJS.experiment.removeLoop(trial_PR);

  return Scheduler.Event.NEXT;
}


var _key_resp_2_allKeys;
var InstruccionesComponents;
function InstruccionesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Instrucciones'-------
    t = 0;
    InstruccionesClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    image.setImage(instrucciones_pasiva);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    InstruccionesComponents = [];
    InstruccionesComponents.push(image);
    InstruccionesComponents.push(key_resp_2);
    
    InstruccionesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function InstruccionesRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Instrucciones'-------
    // get current time
    t = InstruccionesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }

    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
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
    InstruccionesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function InstruccionesRoutineEnd() {
  return async function () {
    //------Ending Routine 'Instrucciones'-------
    InstruccionesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    key_resp_2.stop();
    // the Routine "Instrucciones" was not non-slip safe, so reset the non-slip timer
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
    
    firstfix_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    firstfix_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    firstfix_trainingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    digitpresentation_training.setText(digits_train.toString()[train_digitloopPR.thisN]);
    // keep track of which components have finished
    presentation_trainingComponents = [];
    presentation_trainingComponents.push(digitpresentation_training);
    
    presentation_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    presentation_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    presentation_trainingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var answer_trainPR;
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
    answer_trainPR = Number.parseInt(answer_train);
    
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    recall_trainingComponents = [];
    recall_trainingComponents.push(recall_train);
    recall_trainingComponents.push(answ_train);
    
    recall_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
        if ((answ_train.text === answer_trainPR.toString())) {
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
    recall_trainingComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    recall_trainingComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    post_recall_trainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    post_recall_trainComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    post_recall_trainComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    
    start_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    if (t >= 0.0 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
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
    start_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    start_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
    first_fix.setText('+');
    // keep track of which components have finished
    first_fixationComponents = [];
    first_fixationComponents.push(driftPR);
    first_fixationComponents.push(startPR);
    first_fixationComponents.push(first_fix);
    
    first_fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
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
    
    // *first_fix* updates
    if (t >= 0.5 && first_fix.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      first_fix.tStart = t;  // (not accounting for frame time here)
      first_fix.frameNStart = frameN;  // exact frame index
      
      first_fix.setAutoDraw(true);
    }

    frameRemains = 0.5 + fixation_time - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (first_fix.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      first_fix.setAutoDraw(false);
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
    first_fixationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
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
    first_fixationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    startPR.stop();  // ensure sound has stopped at end of routine
    // the Routine "first_fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var PresentationComponents;
function PresentationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Presentation'-------
    t = 0;
    PresentationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    pres_text.setText(digits.toString()[digitLoop_PR.thisN]);
    // keep track of which components have finished
    PresentationComponents = [];
    PresentationComponents.push(pres_text);
    
    PresentationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function PresentationRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Presentation'-------
    // get current time
    t = PresentationClock.getTime();
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
    PresentationComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function PresentationRoutineEnd() {
  return async function () {
    //------Ending Routine 'Presentation'-------
    PresentationComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    return Scheduler.Event.NEXT;
  };
}


var answer_PR;
var previous_count;
var current_count;
var RecallComponents;
function RecallRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Recall'-------
    t = 0;
    RecallClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    answer_box.setText('');
    answer_box.refresh();
    answer_PR = Number.parseInt(answer_PR);
    previous_count = 0;
    current_count = 0;
    
    // this is a temporary fix to allow editable textbox to be used on several trials
    textbox.refresh()
    // keep track of which components have finished
    RecallComponents = [];
    RecallComponents.push(recall_txt);
    RecallComponents.push(answer_box);
    
    RecallComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function RecallRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Recall'-------
    // get current time
    t = RecallClock.getTime();
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
        if ((answer_box.text === answer_PR.toString())) {
            correct = 1;
        } else {
            correct = 0;
        }
        trial_trainingPR.addData("correct", correct);
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
    RecallComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function RecallRoutineEnd() {
  return async function () {
    //------Ending Routine 'Recall'-------
    RecallComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('answer_box.text',answer_box.text)
    if (((trial_PR.thisTrialN === 0) || (trial_PR.thisTrialN === 1))) {
        if ((correct === 1)) {
            previous_count += 1;
            console.log(` trial = ${trial_PR.thisTrialN} previous_count = ${previous_count}`);
        }
    } else {
        if (((trial_PR.thisTrialN === 2) || (trial_PR.thisTrialN === 3))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_PR.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_PR.thisTrialN === 3)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_PR.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_PR.thisTrialN === 4) || (trial_PR.thisTrialN === 5))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_PR.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_PR.thisTrialN === 5)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_PR.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_PR.thisTrialN === 6) || (trial_PR.thisTrialN === 7))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_PR.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_PR.thisTrialN === 7)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_PR.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_PR.thisTrialN === 8) || (trial_PR.thisTrialN === 9))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_PR.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_PR.thisTrialN === 9)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_PR.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_PR.thisTrialN === 10) || (trial_PR.thisTrialN === 11))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_PR.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_PR.thisTrialN === 11)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_PR.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    } else {
        if (((trial_PR.thisTrialN === 12) || (trial_PR.thisTrialN === 13))) {
            if ((correct === 1)) {
                current_count += 1;
                console.log(` trial = ${trial_PR.thisTrialN} current_count = ${current_count}`);
            }
        }
    }
    if ((trial_PR.thisTrialN === 13)) {
        if (((current_count === 0) && (previous_count === 0))) {
            parar_el_trial = true;
            console.log(`parar_el_trial = ${parar_el_trial}`);
        } else {
            previous_count = current_count;
            current_count = 0;
        }
        console.log(` trial = ${trial_PR.thisTrialN} previous_count = ${previous_count} current_count = ${current_count} parar_el_trial = ${parar_el_trial}`);
    }
    
    // the Routine "Recall" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var post_recallPRComponents;
function post_recallPRRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'post_recallPR'-------
    t = 0;
    post_recallPRClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    post_recallPRComponents = [];
    post_recallPRComponents.push(postrecallPR);
    
    post_recallPRComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function post_recallPRRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'post_recallPR'-------
    // get current time
    t = post_recallPRClock.getTime();
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
    post_recallPRComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function post_recallPRRoutineEnd() {
  return async function () {
    //------Ending Routine 'post_recallPR'-------
    post_recallPRComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    if (parar_el_trial) {
        trial_PR.finished = true;
    }
    
    return Scheduler.Event.NEXT;
  };
}


var LickertComponents;
function LickertRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'Lickert'-------
    t = 0;
    LickertClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    dif_licker.reset()
    // keep track of which components have finished
    LickertComponents = [];
    LickertComponents.push(Dificultad);
    LickertComponents.push(dif_licker);
    
    LickertComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function LickertRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'Lickert'-------
    // get current time
    t = LickertClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Dificultad* updates
    if (t >= 0.0 && Dificultad.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Dificultad.tStart = t;  // (not accounting for frame time here)
      Dificultad.frameNStart = frameN;  // exact frame index
      
      Dificultad.setAutoDraw(true);
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
    LickertComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function LickertRoutineEnd() {
  return async function () {
    //------Ending Routine 'Lickert'-------
    LickertComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('dif_licker.response', dif_licker.getRating());
    psychoJS.experiment.addData('dif_licker.rt', dif_licker.getRT());
    // the Routine "Lickert" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var EndComponents;
function EndRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //------Prepare to start Routine 'End'-------
    t = 0;
    EndClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(3.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    EndComponents = [];
    EndComponents.push(thank_you);
    
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function EndRoutineEachFrame() {
  return async function () {
    //------Loop for each frame of Routine 'End'-------
    // get current time
    t = EndClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *thank_you* updates
    if (t >= 0.0 && thank_you.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      thank_you.tStart = t;  // (not accounting for frame time here)
      thank_you.frameNStart = frameN;  // exact frame index
      
      thank_you.setAutoDraw(true);
    }

    frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (thank_you.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      thank_you.setAutoDraw(false);
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
    EndComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function EndRoutineEnd() {
  return async function () {
    //------Ending Routine 'End'-------
    EndComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
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
