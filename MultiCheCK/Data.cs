using System.ComponentModel.DataAnnotations;
using Microsoft.EntityFrameworkCore;

public class MultasDbContext : DbContext
{
    public MultasDbContext(DbContextOptions<MultasDbContext> options) : base(options) { }

    public DbSet<Usuario> Usuarios { get; set; }
    public DbSet<Multa> Multas { get; set; }
    public DbSet<ConceptoMulta> ConceptosMultas { get; set; }
    public DbSet<Comision> Comisiones { get; set; }

    public DbSet<ReporteIngreso> ReportesIngreso { get; set; }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
   {
        base.OnModelCreating(modelBuilder);

        // Relación entre Multa y Comision
        modelBuilder.Entity<Multa>()
            .HasMany(m => m.Comisiones)  // Multa tiene muchas Comisiones
            .WithOne(c => c.Multa)       // Cada Comision está asociada a una Multa
            .HasForeignKey(c => c.MultaId); // La clave foránea es MultaId

        modelBuilder.Entity<Usuario>().HasData(
            new Usuario { Id = 1, Cedula = "admin123", Nombre = "Admin", Clave = "estoesfacil", Rol = "Administrador", Activo = true }
        );
    }
     public async Task<(double TotalComision, List<Comision> UltimosAportes)> GetComisionesPorAgenteMes(int agenteId, int mes, int año)
    {
        var comisiones = await Comisiones
            .Where(c => c.AgenteId == agenteId && c.Mes == mes && c.Año == año)
            .OrderByDescending(c => c.Id)
            .ToListAsync();

        double  totalComision = Convert.ToDouble(comisiones.Sum(c => c.Monto));
        var ultimosAportes = comisiones.Take(5).ToList();

        return (totalComision, ultimosAportes);
    }
    

}

public class Usuario
{
    public int Id { get; set; }
    public string Cedula { get; set; }
    public string Nombre { get; set; }

    [Required(ErrorMessage = "La clave es obligatoria.")]
    [MinLength(6, ErrorMessage = "La clave debe tener al menos 6 caracteres.")]
    public string Clave { get; set; }
    public string Rol { get; set; }  // Agente, OficinaCentral, Administrador
    public bool Activo { get; set; }
}



public class Multa
{
    public int Id { get; set; }
    public string CedulaCiudadano { get; set; }
    public string NombreCiudadano { get; set; }
    public int ConceptoId { get; set; } // Referencia al tipo de multa (sin relación)
    public ConceptoMulta Concepto { get; set; }
    public string Descripcion { get; set; }
    public double Latitud { get; set; }
    public double Longitud { get; set; }
    public byte[]? Foto { get; set; } 
    public DateTime FechaRegistro { get; set; } = DateTime.Now;
    public string Estado { get; set; } = "Activa"; // Activa, Perdona, Pagada
    public int AgenteId { get; set; }  // Referencia al agente que registró la multa (sin relación)
    public ICollection<Comision> Comisiones { get; set; }
}


public class ConceptoMulta
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public string Descripcion { get; set; }
}



public class Comision
{
    public int Id { get; set; }
    public int AgenteId { get; set; }  // Referencia al agente que recibe la comisión
    public int MultaId { get; set; }   // Referencia a la multa que generó la comisión
    public double Monto { get; set; }
    public int Mes { get; set; }
    public int Año { get; set; }
    public Multa Multa { get; set; }
}

public class ReporteIngreso
{
    public int Id { get; set; }
    public int Mes { get; set; }
    public int Año { get; set; }
    public decimal Total { get; set; }
    public string TipoMulta { get; set; }
    public int Cantidad { get; set; }
}


