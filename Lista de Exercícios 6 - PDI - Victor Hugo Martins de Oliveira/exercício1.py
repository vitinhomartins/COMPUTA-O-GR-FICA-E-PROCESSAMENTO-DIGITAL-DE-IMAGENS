
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angulo = 0
perspectiva = False

def desenhaGrade():
    glColor3f(0.8, 0.8, 0.8)

    glBegin(GL_LINES)

    for i in range(-5, 6):
        glVertex3f(i, -5, 0)
        glVertex3f(i, 5, 0)

        glVertex3f(-5, i, 0)
        glVertex3f(5, i, 0)

    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(0, 0, -12)

    glRotatef(angulo, 1, 0, 0)

    desenhaGrade()

    glutSwapBuffers()


def reshape(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    aspect = width / height

    if perspectiva:
        gluPerspective(60, aspect, 1, 50)
    else:
        glOrtho(-6 * aspect, 6 * aspect, -6, 6, -50, 50)

    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    global perspectiva

    if key == b'p':
        perspectiva = not perspectiva
        reshape(glutGet(GLUT_WINDOW_WIDTH),
                glutGet(GLUT_WINDOW_HEIGHT))

    elif key == b'q':
        glutDestroyWindow(glutGetWindow())
        return

    glutPostRedisplay()


def keySpecial(key, x, y):
    global angulo

    if key == GLUT_KEY_UP:
        angulo += 5

    elif key == GLUT_KEY_DOWN:
        angulo -= 5

    glutPostRedisplay()


def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Exercicio 1 - Grade 3D")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keySpecial)

    glutMainLoop()


if __name__ == "__main__":
    main()
