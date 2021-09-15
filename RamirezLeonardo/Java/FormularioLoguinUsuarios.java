package co.com.loguinfacturacion.basedatos;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.SwingConstants;
import java.awt.Font;
import javax.swing.JTextField;
import javax.swing.JPasswordField;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.awt.event.ActionEvent;

public class FormularioLoguinUsuarios extends JFrame {

	private JPanel contentPane;
	private JTextField textUsuario;
	private JPasswordField TextPass;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					FormularioLoguinUsuarios frame = new FormularioLoguinUsuarios();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public FormularioLoguinUsuarios() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		JLabel lblNewLabel = new JLabel("Loguin Facturacion");
		lblNewLabel.setFont(new Font("Cambria Math", Font.PLAIN, 16));
		lblNewLabel.setHorizontalAlignment(SwingConstants.CENTER);
		lblNewLabel.setBounds(131, 27, 154, 33);
		contentPane.add(lblNewLabel);
		
		JLabel labelUser = new JLabel("Usuario: ");
		labelUser.setFont(new Font("Cambria Math", Font.PLAIN, 16));
		labelUser.setBounds(84, 97, 100, 33);
		contentPane.add(labelUser);
		
		JLabel labelPass = new JLabel("Contrase\u00F1a: ");
		labelPass.setFont(new Font("Cambria Math", Font.PLAIN, 16));
		labelPass.setBounds(84, 141, 100, 33);
		contentPane.add(labelPass);
		
		textUsuario = new JTextField();
		textUsuario.setBounds(194, 103, 145, 20);
		contentPane.add(textUsuario);
		textUsuario.setColumns(10);
		
		TextPass = new JPasswordField();
		TextPass.setBounds(194, 147, 145, 20);
		contentPane.add(TextPass);
		
		JButton ButtonLoguin = new JButton("Iniciar Sesi\u00F3n");
		ButtonLoguin.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				try {
					ConsultaBD Con = new ConsultaBD();
					String u = textUsuario.getText();
					String p = TextPass.getText();
					Con.conectarBD();
					String sentencia = "SELECT id, nickname FROM usuarios WHERE nickname='" + u + "' AND pass='" + p + "'";
					Con.resultado = Con.sentencia.executeQuery(sentencia);
					
					//int intentosMax = 3
					//int cont = 3
					//if cont < 
					
						if(Con.resultado.next()) {
							setVisible(false);
							FormularioPrincipal Principal = new FormularioPrincipal();
							Principal.setVisible(true);
							
						}else {
							JOptionPane.showMessageDialog(null, "Usuario o contraseña invalido");
						}
					
				} catch (SQLException ex) {
					JOptionPane.showMessageDialog(null, ex.getMessage());
				}
			}
		});
		ButtonLoguin.setFont(new Font("Cambria Math", Font.PLAIN, 16));
		ButtonLoguin.setBounds(141, 185, 154, 23);
		contentPane.add(ButtonLoguin);
	}
}
