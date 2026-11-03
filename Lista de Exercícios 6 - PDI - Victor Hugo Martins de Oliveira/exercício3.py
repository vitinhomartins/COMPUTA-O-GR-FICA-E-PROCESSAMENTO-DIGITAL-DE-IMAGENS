from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

distance = 8.0
azimuth = 0.0
incidence = 20.0
twist = 0.0

botaoAtivo = None
ultimoX = 0
ultimoY = 0


def polarView(distance, azimuth, incidence, twist):
    glTranslatef(0.0, 0.0, -distance)
    glRotatef(-twist, 0.0, 0.0, 1.0)
    glRotatef(-incidence, 1.0, 0.0, 0.0)
    glRotatef(-azimuth, 0.0, 0.0, 1.0)


def desenhaEixos():
    glBegin(GL_LINES)

    # Eixo X - vermelho
    glColor3f(1, 0, 0)
    glVertex3f(-3, 0, 0)
    glVertex3f(3, 0, 0)

    # Eixo Y - verde
    glColor3f(0, 1, 0)
    glVertex3f(0, -3, 0)
    glVertex3f(0, 3, 0)

    # Eixo Z - azul
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, -3)
    glVertex3f(0, 0, 3)

    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    polarView(distance, azimuth, incidence, twist)

    desenhaEixos()

    glColor3f(1, 1, 0)
    glutWireTeapot(1.0)

    glutSwapBuffers()


def reshape(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(60, width / height, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)


def mouse(button, state, x, y):
    global distance, botaoAtivo, ultimoX, ultimoY

    if button == 3 and state == GLUT_DOWN:
        distance -= 0.5

        if distance < 2:
            distance = 2

    elif button == 4 and state == GLUT_DOWN:
        distance += 0.5

    elif state == GLUT_DOWN:
        botaoAtivo = button
        ultimoX = x
        ultimoY = y

    elif state == GLUT_UP:
        botaoAtivo = None

    glutPostRedisplay()


def mouseMotion(x, y):
    global azimuth, incidence, twist
    global ultimoX, ultimoY

    dx = x - ultimoX
    dy = y - ultimoY

    if botaoAtivo == GLUT_LEFT_BUTTON:
        azimuth += dx
        incidence += dy

        if incidence > 89:
            incidence = 89

        if incidence < -89:
            incidence = -89

    elif botaoAtivo == GLUT_RIGHT_BUTTON:
        twist += dx

    ultimoX = x
    ultimoY = y

    glutPostRedisplay()


def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"Exercicio 3 - Camera Polar")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMouseFunc(mouse)
    glutMotionFunc(mouseMotion)

    glutMainLoop()


if __name__ == "__main__":
    main()