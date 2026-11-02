#게임 월드 리스트

world = [ [], []] # 0번은 잔디, 1번은 소년과 공을 담는 레이어

#객체를 게임월드에 추가하는 함수
def add_object(o, depth): # depth는 객체를 넣을 레이어 번호
    world[depth].append(o) # 선택한 레이어에 객체 추가

#게임 로직
def update():
    for layer in world: # 객체가 들어 있는 레이어를 하나씩 꺼냄
        for o in layer[:]: # 삭제 중 다음 객체를 건너뛰지 않도록 복사본 순회
            o.update() # 이동 등 객체의 상태 갱신



def remove_object(o):
    for layer in world: #모든 레이어를 순회하면서 객체를 제거
        if o in layer:  #객체가 해당 레이어에 존재하면 제거
            layer.remove(o) # 해당 레이어에서 객체 제거
            return  #제거 후 함수 종료

#게임 월드 렌더링

def render():
    for layer in world: # 0번부터 그려 뒤쪽과 앞쪽 순서를 정함
        for o in layer: # 해당 레이어 안의 객체를 하나씩 꺼냄
            o.draw() # 객체를 화면에 그림