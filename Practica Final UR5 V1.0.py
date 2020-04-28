# PROYECT:  Programación Robot UR5 (Universal Robots)

# DESIGNER: Jesus Alguacil Mérida

# UPDATE:   22/03/2020

# Comenzamos inicializando y verificando todos los sistemas


set_gravity([0.0, 0.0, 9.82])
set_safety_mode_transition_hardness(1)
set_tcp(p[0.0,0.0,0.02,0.0,0.0,0.0])
set_payload(0.2,[0.0,0.0,0.02])
set_standard_analog_input_domain(0, 1)
set_standard_analog_input_domain(1, 1)
set_tool_analog_input_domain(0, 1)
set_tool_analog_input_domain(1, 1)
set_analog_outputdomain(0, 1)
set_analog_outputdomain(1, 1)
set_input_actions_to_default()
set_tool_voltage(0)
global temporizador_1=0
global temporizador_2=0 
global temporizador_3=0
global temporizador_2_is_counting=False
global temporizador_1_is_counting=False
global temporizador_3_is_counting=False
thread Timer_Thread():

# INSTRUCCIÓN WHILE
# Con la instruccion while le decimos que nos repita en bucle la inicializacion de los temporizadores
    while (True):
      # Declaramos las instruciones (IF) para inicializar la instruccion de temporizadores
      # Temporizador correspondiente al cuadrado Nº1
      if (temporizador_1_is_counting):
        temporizador_1 = temporizador_1 + get_steptime()
      end
      # Temporizador correspondiente al cuadrado Nº2
      if (temporizador_2_is_counting):
        temporizador_2 = temporizador_2 + get_steptime()
      end
      # Temporizador correspondiente al cuadrado Nº3
      if (temporizador_3_is_counting):3

        temporizador_3 = temporizador_3 + get_steptime()
      end
      sync()
    end
  end
  run Timer_Thread()

# INICIAMOS EL PROGRAMA  

# INSTRUCCIÓN WHILE
# Para la primera parte del programa utilizamos una instruccion while para un movimiento en bucle
  while (True):

# Iniciamos la comprobacion con un (IF), para que haga un trabajo u otro dependiendo de si la entrada digital 1 esta en "True" o "False"
    if (get_standard_digital_in(1) ==   True  ):

# Inicializamos el trabajo numero (1) del robot que ejecutara el codigo script si la entrada digital esta en "True" de ser "False" se inicializara el trabajo numero (2) del robot
      # PUNTO 1º El primer punto en el espacio se trata del punto inicial o "HOME" de donde partira y terminara todos los movimientos del robot
      movej(get_inverse_kin(p[-.120113156097, -.173771525008, .302072499570, -.001221338502, 3.116276491019, .038892424546], qnear=[-1.6431244055377405, -0.7782180945025843, -2.365068022404806, -1.5958216826068323, 1.5939878225326538, -0.07342178026308233]), a=0.1, v=0.2)

      # PUNTO 2º iniciamos un (SET) sobre la salida analógica numero 1 y la alimentamos con 5V 
      set_standard_analog_out(1, 0.5)

      # PUNTO 3º Realizamos un (MoveJ) con 2 puntos de paso (Punto de Paso "1")
      movej(get_inverse_kin(p[-.120113150197, -.235363202025, .463264144654, -.001221396485, 3.116276467505, .038891955098], qnear=[-1.624932114277975, -0.9993456045733851, -1.8808558622943323, -1.8584798018084925, 1.5944700241088867, -0.05523091951479131]), a=1.3962634015954636, v=1.0471975511965976)
       # (Punto de Paso "2")
      movej(get_inverse_kin(p[-.120113226303, -.390154760215, .378072482731, -.001221164641, 3.116276503821, .038891991581], qnear=[-1.6038430372821253, -1.3608463446246546, -1.888193432484762, -1.4891365210162562, 1.5950191020965576, -0.03414279619325811]), a=1.3962634015954636, v=1.0471975511965976)
      
      # PUNTO 4º Iniciamos un (SET) sobre la salida digital "0" de la herramienta y la ponemos en "True"
      set_tool_digital_out(0, True)
      
      # PUNTO 5º Iniciamos un (SET) sobre la salida analógica numero 1 y la alimentamos con 0V
      set_standard_analog_out(1, 0.0)
      
      # PUNTO 6º Iniciamos una instruccion de espera de "2 Segundos"
      sleep(2.0)
      
      # PUNTO 7º Iniciamos un (SET) sobre la salida analógica numero 1 y la alimentamos con 10V
      set_standard_analog_out(1, 1.0)
      
      # PUNTO 8º Realizamos un (MoveJ) con 2 puntos de paso (Punto de Paso "3")
      movej(get_inverse_kin(p[-.120113150197, -.235363202025, .463264144654, -.001221396485, 3.116276467505, .038891955098], qnear=[-1.624932114277975, -0.9993456045733851, -1.8808558622943323, -1.8584798018084925, 1.5944700241088867, -0.05523091951479131]), a=1.3962634015954636, v=1.0471975511965976)
       # (Punto de paso "4")
      movej(get_inverse_kin(p[-.120113156097, -.173771525008, .302072499570, -.001221338502, 3.116276491019, .038892424546], qnear=[-1.6431244055377405, -0.7782180945025843, -2.365068022404806, -1.5958216826068323, 1.5939878225326538, -0.07342178026308233]), a=1.3962634015954636, v=1.0471975511965976)
      
      # PUNTO 9º Iniciamos un (SET) sobre la salida digital "0" de la herramienta y la ponemos en "False"
      set_tool_digital_out(0, False)
      
      # PUNTO 10º En este punto se muestra un mensaje indicando si se desea continuar (El programa se detendra hasta que el operario lo indique) en caso contrario el programa del trabajo 1 finaliza
      popup("'Proceso 1 Terminado. ¿Desea continuar?'", "Mensaje", False, False, blocking=True)

# Con el (ElsIf) le indicamos que que si no se cumple la condicion de arriba se ejecute el siguiente codigo script
    else:
        # Iniciamos la comprobacion con un (IF), para que haga un trabajo u otro dependiendo de si la entrada digital 1 esta en "True" o "False"
      if (get_standard_digital_in(1) ==   False  ):

# Inicializamos el trabajo numero (2) del robot que ejecutara el codigo script si la entrada digital esta en "False"
      # PUNTO 1º Restablecemos los 3 temporizadores a "0"
        temporizador_1 = 0
      
        temporizador_2 = 0 
      
        temporizador_3 = 0 
    
      # PUNTO 2º Restablecemos a "0" la salida analogica 1 del anterior trabajo
        set_standard_analog_out(1, 0.0)

      # PUNTO 3º El primer punto en el espacio se trata del punto inicial o "HOME" de donde partira y terminara todos los movimientos del robot
        movej(get_inverse_kin(p[-.120113156097, -.173771525008, .302072499570, -.001221338502, 3.116276491019, .038892424546], qnear=[-1.6431244055377405, -0.7782180945025843, -2.365068022404806, -1.5958216826068323, 1.5939878225326538, -0.07342178026308233]), a=0.1, v=0.2)

      # PUNTO 4º Realizamos un (MovJ) con 2 puntos de paso para posicionarlo en un cuadrado (Punto de Paso "1")
        movej(get_inverse_kin(p[-.120113076222, -.216246420400, .427955918672, -.001221375727, 3.116276450478, .038892186341], qnear=[-1.6316188017474573, -0.9465745131122034, -1.9407027403460901, -1.8515618483172815, 1.5942937135696411, -0.06191713014711553]), a=1.3962634015954636, v=1.0471975511965976)
        # (Punto de Paso "2")
        movej(get_inverse_kin(p[-.397688279532, -.356708694019, .504734878271, .028564196418, -2.225781256862, 2.163633968976], qnear=[-2.3368502298938196, -1.7453692595111292, -1.6399992148028772, 0.20539002120494843, 2.322514295578003, -0.06585389772524053]), a=1.3962634015954636, v=1.0471975511965976)

      # PUNTO 5º Iniciamos un (SET) sobre la salida digital "1" de la herramienta y la ponemos en "True"
        set_tool_digital_out(1, True)
      
      # PUNTO 6º Iniciamos un set en el "Temporizador 1" que marcara el tiempo de ejecucion del cuadrado Nº1
        temporizador_1_is_counting = True
      
      # PUNTO 7º Iniciamos el movimiento con forma cuadrada mediante un (MovP) con 4 puntos de paso (Punto de paso "1") con una duracion de "16" Segundos
        movel(p[-.397688233897, -.356708646525, .704729959326, .028564290721, -2.225781107143, 2.163634027694], t=4.0)
        # (Punto de paso "2")
        movel(p[-.197690056869, -.356708822265, .704729787391, .028564049143, -2.225782050473, 2.163633379960], t=4.0)
        # (Punto de paso "3")
        movel(p[-.197690049538, -.356708799550, .504729949596, .028564018959, -2.225782170636, 2.163633289537], t=4.0)
        # (Punto de paso "4")
        movel(p[-.397688279532, -.356708694019, .504734878271, .028564196418, -2.225781256862, 2.163633968976], t=4.0)
        
      # PUNTO 8º Iniciamos un reset en el "Temporizador 1" que marcara el tiempo de ejecucion del cuadrado Nº1
        temporizador_1_is_counting = False
      
      # PUNTO 9º Iniciamos un set en el "Temporizador 2" que marcara el tiempo de ejecucion del cuadrado Nº2
        temporizador_2_is_counting = True
      
      # PUNTO 10º Iniciamos el movimiento con forma cuadrada mediante un (MovP) con 4 puntos de paso (Punto de paso "1") con una duracion de "8" Segundos
        movel(p[-.397688173259, -.356708583494, .704730034007, .028564454075, -2.225780248207, 2.163634696738], t=2.0)
        # (Punto de paso "2")
        movel(p[-.197690056869, -.356708822265, .704729787391, .028564049143, -2.225782050473, 2.163633379960], t=2.0)
        # (Punto de paso "3")
        movel(p[-.197690049538, -.356708799550, .504729949596, .028564018959, -2.225782170636, 2.163633289537], t=2.0)
        # (Punto de paso "4")
        movel(p[-.397688279532, -.356708694019, .504734878271, .028564196418, -2.225781256862, 2.163633968976], t=2.0)
      
      # PUNTO 11º Iniciamos un reset en el "Temporizador 2" que marcara el tiempo de ejecucion del cuadrado Nº2
        temporizador_2_is_counting = False
      
      # PUNTO 12º Iniciamos un set en el "Temporizador 3" que marcara el tiempo de ejecucion del cuadrado Nº3
        temporizador_3_is_counting = True
      
      # PUNTO 13º Iniciamos el movimiento con forma cuadrada mediante un (MovP) con 4 puntos de paso (Punto de paso "1") con una duracion de "4" Segundos
        movel(p[-.397688233897, -.356708646525, .704729959326, .028564290721, -2.225781107143, 2.163634027694], t=1.0)
        # (Punto de paso "2")
        movel(p[-.197690056869, -.356708822265, .704729787391, .028564049143, -2.225782050473, 2.163633379960], t=1.0)
        temporizador_3_is_counting = False
        movel(p[-.197690049538, -.356708799550, .504729949596, .028564018959, -2.225782170636, 2.163633289537], t=1.0)
        # (Punto de paso "4")
        movel(p[-.397688279532, -.356708694019, .504734878271, .028564196418, -2.225781256862, 2.163633968976], t=1.0)
        # (Punto de paso "3")
      
      # PUNTO 14º Iniciamos un reset en el "Temporizador 2" que marcara el tiempo de ejecucion del cuadrado Nº2
      
      # PUNTO 15º Iniciamos un (SET) sobre la salida digital "1" de la herramienta y la ponemos en "False"
        set_tool_digital_out(1, False)

      # PUNTO 16º Realizamos un (MovJ) con 2 puntos de paso para posicionarlo en el punto "HOME" (Punto de Paso "1")
        movej(get_inverse_kin(p[-.120113076222, -.216246420400, .427955918672, -.001221375727, 3.116276450478, .038892186341], qnear=[-1.6316188017474573, -0.9465745131122034, -1.9407027403460901, -1.8515618483172815, 1.5942937135696411, -0.06191713014711553]), a=1.3962634015954636, v=1.0471975511965976)
        # (Punto de paso "2")
        movej(get_inverse_kin(p[-.120113156097, -.173771525008, .302072499570, -.001221338502, 3.116276491019, .038892424546], qnear=[-1.6431244055377405, -0.7782180945025843, -2.365068022404806, -1.5958216826068323, 1.5939878225326538, -0.07342178026308233]), a=1.3962634015954636, v=1.0471975511965976)
      
      # PUNTO 17º En este punto se muestra un mensaje indicando que el trabajo o "Proceso" a finalizado
        popup("Proceso Finalizado", "Mensaje", False, False, blocking=False)
        halt
      end
    end
  end
end
