package co.com.loguinfacturacion.basedatos;

import java.sql.*;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import javax.swing.JOptionPane;


public class ConsultaBD {
	
	public Connection conexion;
    public Statement sentencia;
    public ResultSet resultado;
	
	
	public void conectarBD() {

		try {
            
			
			Class.forName("com.mysql.cj.jdbc.Driver");
			String url = "jdbc:Mysql://localhost:3306/loguinusuarios";
			Connection conexion = DriverManager.getConnection(url, "root", "********");
                                                                            // ^ aqui va la contraseña de la base de datos
			
            sentencia = conexion.createStatement();
            
            
            
        } catch (ClassNotFoundException | SQLException ex) {
            JOptionPane.showMessageDialog(null, ex.getMessage(), "Error ", JOptionPane.ERROR_MESSAGE);
        }
    }

    //public void DesconectarBasedeDatos() {
    //    try {
    //        if (conexion != null) {
    //            if (sentencia != null) {
    //                sentencia.close();
    //            }
    //            conexion.close();
    //        }
    //    } catch (SQLException ex) {
    //        JOptionPane.showMessageDialog(null, ex.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
    //        System.exit(1);
    //    }
    //}

    //public Connection getConnection() {
    //    return conexion;
    //}
}
