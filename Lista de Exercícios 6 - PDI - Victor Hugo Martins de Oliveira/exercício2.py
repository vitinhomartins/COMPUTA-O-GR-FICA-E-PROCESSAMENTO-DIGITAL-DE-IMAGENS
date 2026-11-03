from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

rotacaoBraco = 0
aberturaGarra = 20


def wireBox(dx, dy, dz):
    glPushMatrix()

    glTranslatef(dx / 2, 0, 0)
    glScalef(dx, dy, dz)

    glutWireCube(1)

    glPopMatrix()


def desenhaBraco():
    glPushMatrix()

    # Base do braço
    glColor3f(0.7, 0.7, 0.7)
    glutWireCube(0.6)

    # Rotação do braço inteiro a partir da base
    glRotatef(rotacaoBraco, 0, 0, 1)

    # Parte principal do braço
    glColor3f(0.2, 0.8, 1.0)
    wireBox(3.0, 0.4, 0.4)

    # Desloca até a extremidade do braço
    glTranslatef(3.0, 0, 0)

    # Articulação da garra
    glColor3f(1.0, 1.0, 0.0)
    glutWireCube(0.3)

    # Ponta superior
    glPushMatrix()
    glTranslatef(0, 0.15, 0)
    glRotatef(aberturaGarra, 0, 0, 1)
    glColor3f(1.0, 0.3, 0.3)
    wireBox(1.2, 0.18, 0.18)
    glPopMatrix()

    # Ponta inferior
    glPushMatrix()
    glTranslatef(0, -0.15, 0)
    glRotatef(-aberturaGarra, 0, 0, 1)
    glColor3f(0.3, 1.0, 0.3)
    wireBox(1.2, 0.18, 0.18)
    glPopMatrix()

    glPopMatrix()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(-1.5, 0, -8)

    desenhaBraco()

    glutSwapBuffers()


def reshape(width, height):
    if height == 0:
        height = 1

    glViewport(0, 0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    aspecto = width / height

    glOrtho(
        -5 * aspecto, 5 * aspecto,
        -5, 5,
        -20, 20
    )

    glMatrixMode(GL_MODELVIEW)


def keyboard(key, x, y):
    global aberturaGarra

    if key == b'o':
        aberturaGarra += 5

        if aberturaGarra > 45:
            aberturaGarra = 45

    elif key == b'f':
        aberturaGarra -= 5

        if aberturaGarra < 0:
            aberturaGarra = 0

    elif key == b'q':
        glutDestroyWindow(glutGetWindow())
        return

    glutPostRedisplay()


def keySpecial(key, x, y):
    global rotacaoBraco

    if key == GLUT_KEY_LEFT:
        rotacaoBraco += 5

    elif key == GLUT_KEY_RIGHT:
        rotacaoBraco -= 5

    glutPostRedisplay()


def init():
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)

    glutInitWindowSize(800, 600)
    glutInitWindowPosition(100, 100)

    glutCreateWindow(b"Exercicio 2 - Garra Robotica")

    init()

    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(keySpecial)

    glutMainLoop()


if __name__ == "__main__":
    main()