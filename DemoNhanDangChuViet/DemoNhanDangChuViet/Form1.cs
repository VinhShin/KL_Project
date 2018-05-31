using Emgu.CV;
using Emgu.CV.Features2D;
using Emgu.CV.Structure;
using Emgu.CV.Util;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Windows.Forms;


namespace DemoNhanDangChuViet
{
    public partial class Form1 : Form
    {
        List<SinhVien> lst = new List<SinhVien>();
        Image image;
        string path = "";
        static Bitmap bmp = null;
        public Image Image
        {
            get { return image; }
            set { image = value; }
        }
        string line;
        public Form1()
        {
            InitializeComponent();
        }
        OpenFileDialog ofd = new OpenFileDialog();
        private void btInputImage_Click(object sender, EventArgs e)
        {
            removeBitMap();
            ofd.Title = "Open Image";
            ofd.InitialDirectory = @""+Constant.currentPath+"";
            ofd.Filter = "Image |*.png";
            
            if (ofd.ShowDialog() == DialogResult.OK)
            {
//                image = Image.FromFile(ofd.FileName);
                path = ofd.FileName;
                //pictureBox1.Image = Image.FromFile(ofd.FileName);
            }
            Constant.pathImage = path;
            string[] name = Constant.pathImage.Split('\\');
            string[] bangdiem = name[name.Length - 1].Split('.');

            Constant.bangdiem = bangdiem[0];

            //fShowImage f = new fShowImage(path);
            Bitmap bmp=null;
            try
            {
                bmp = new Bitmap(@"" + path + "");
            }
            catch (Exception ed) { 
            }
            pictureBox1.Image = bmp;
            //f.setPath(path);
            //f.Show();
        }
        private void removeBitMap()
        {
           if (bmp != null)
               bmp.Dispose();
             
        }

        private void btRead_Click(object sender, EventArgs e)
        {

            richTextBox1.Text = "";
            lst.Clear();
            SinhVien[] arr= new SinhVien[100];
            System.IO.StreamReader file = new System.IO.StreamReader(Constant.currentPath+"//Output.txt");
            while ((line = file.ReadLine()) != null)
            {
                string[] words = line.Split('\t');
                lst.Add(new SinhVien( words[0].Trim(), words[1].Trim(), words[2].Trim()));
                
            }
            file.Close();
            for (int i = 0; i < lst.Count; i++)
            {
                richTextBox1.Text += lst[i].Maso + "\t" + lst[i].Diemso + "\t" + lst[i].Diemchu + "\n";
            }
           
        }

        private void btImportExcel_Click(object sender, EventArgs e)
        {
            int j = 1;
            SaveFileDialog fsave = new SaveFileDialog();
          
            Microsoft.Office.Interop.Excel.Application app = new Microsoft.Office.Interop.Excel.Application();
//            Microsoft.Office.Interop.Excel.Workbook wb = app.Workbooks.Add(Type.Missing);
            Microsoft.Office.Interop.Excel.Workbook wb = app.Workbooks.Open(Constant.currentPath + "//BangDiem.xlsx");
            Microsoft.Office.Interop.Excel._Worksheet sheet = null;
            try
            {
                    
                sheet = wb.ActiveSheet;
                sheet.Name = Constant.bangdiem;
                wb.Worksheets.Add(sheet);
                //                sheet.Name = "Dữ liệu xuất ra";
                sheet.Cells[1, 1].Value = "BẢNG ĐIỂM";
                for (int i = 0; i < lst.Count; i++)
                {
                      
                        sheet.Cells[j + 1, 1].Value = lst[i].Maso;
                        sheet.Cells[j + 1, 2].Value = lst[i].Diemso;
                        sheet.Cells[j + 1, 3].Value = lst[i].Diemchu;
                        j++;
                }
                
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Thông báo", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            finally
            {
                wb.Save();
                wb.Close(true);
                app.Quit();
                wb = null;
            }
           
        }
        Bitmap find_contour(Image<Bgr, Byte> img_mau, Image<Gray, Byte> img_xam)
        {
            img_xam = img_xam.PyrUp().PyrDown();

            Image<Gray, Byte> img_xam_t1 = img_xam.Canny(150, 60);
            Image<Gray, Byte> img_xam_t2 = new Image<Gray, byte>(img_xam.Width, img_xam.Height, new Gray(0));

            double RhoRes, Threshold, MinLineWidth, ThetaRes;
            int linegap;
            RhoRes = 0.5;
            Threshold = 25;
            MinLineWidth = 1;
            linegap = 10;
            ThetaRes = Math.PI / 180;

            LineSegment2D[][] LineSegment2D = img_xam_t1.HoughLinesBinary(RhoRes, ThetaRes, (int)Threshold, MinLineWidth, linegap);
            for (int i = 0; i < LineSegment2D[0].Length - 1; i++)
            {
                img_xam_t2.Draw(LineSegment2D[0][i], new Gray(255), 2);
            }

            using (MemStorage storage = new MemStorage())
                for (Contour<Point> contours = img_xam_t2.FindContours(Emgu.CV.CvEnum.CHAIN_APPROX_METHOD.CV_LINK_RUNS, Emgu.CV.CvEnum.RETR_TYPE.CV_RETR_EXTERNAL, storage); contours != null; contours = contours.HNext)
                {

                    Contour<Point> ct = contours.ApproxPoly(contours.Perimeter * 2, storage);
                    if (ct.Total == 4 && ct.Area == 7000)
                    {
                        Point[] pt = ct.ToArray();
                        img_mau.DrawPolyline(pt, true, new Bgr(Color.Yellow), 4);
                    }

                    //Contour<Point> currentContour = contours.ApproxPoly(contours.Perimeter * 0.05, storage);
                    //img_mau.DrawPolyline(, True, New Bgr(255, 0, 0), 4)
                    //CvInvoke.cvDrawContours(img_mau, contours, new MCvScalar(255), new MCvScalar(255), -1, 1, Emgu.CV.CvEnum.LINE_TYPE.EIGHT_CONNECTED, new Point(0, 0));

                }

            return img_mau.ToBitmap();
        }

        private void btContour_Click(object sender, EventArgs e)
        {
             
        //    Bitmap bm = (Bitmap)pictureBox1.Image;
        //   // Image<Gray, Byte> img_xam = new Image<Gray, Byte>((Bitmap)pictureBox1.Image);//ảnh xám
        //    Image<Bgr, Byte> img = new Image<Bgr, byte>(bm);//ảnh màu
        //   Image<Gray, Byte> img_xam = img.Convert<Gray, Byte>();//ảnh xám
        //   // pictureBox2.Image = img_xam.ToBitmap(pictureBox2.Width, pictureBox2.Height);
        //    pictureBox2.Image = find_contour(img, img_xam);

            ExecuteBatFile();
           // Bitmap bmp = new Bitmap(@"Logos/bitmap.bmp");
           // pictureBox1.Image = bmp;


        }
        private void ExecuteBatFile()
        {
            Process proc = null;
            try
            {
                pictureBox2.Image = null;
                string targetDir = string.Format(Constant.currentPath);   //this is where mybatch.bat lies

                proc = new Process();
                proc.StartInfo.WorkingDirectory = targetDir;
                proc.StartInfo.FileName = "make_contours.bat";
                proc.StartInfo.Arguments = @"" + Constant.pathImage + "";
                proc.StartInfo.CreateNoWindow = false;
      //          proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;  //this is for hiding the cmd window...so execution will happen in back ground.
                proc.Start();
                proc.WaitForExit();
                //bmp = new Bitmap(@"" + Constant.currentPath + "\\bangdiem_contours.png");
                bmp = new Bitmap(@"" + Constant.currentPath + "\\bangdiem_morph_line.png");
                pictureBox2.Image = bmp;
                //                path = @"..\..\DemoNhanDangChuViet\Python_Master\bangdiem_reshape.png";
                ////                path = @"D:\nhandienchuviet\KL_Project\DemoNhanDangChuViet\DemoNhanDangChuViet\Python_Master\bangdiem_reshape.png";
                //                fShowImage f = new fShowImage(path);
                //                f.setPath(path);
                //                f.Show();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception Occurred :{0},{1}", ex.Message, ex.StackTrace.ToString());
            }
        }
        public void ExecuteCommand(string command)
        {
            int ExitCode;
            ProcessStartInfo ProcessInfo;
            Process process;

            ProcessInfo = new ProcessStartInfo(Application.StartupPath + "\\Python_Master\\make_contours.bat", command);
            ProcessInfo.CreateNoWindow = true;
            ProcessInfo.UseShellExecute = false;
            ProcessInfo.WorkingDirectory = Application.StartupPath + "\\Python_Master";
            // *** Redirect the output ***
            ProcessInfo.RedirectStandardError = true;
            ProcessInfo.RedirectStandardOutput = true;

            process = Process.Start(ProcessInfo);
            process.WaitForExit();

            // *** Read the streams ***
            string output = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();

            ExitCode = process.ExitCode;

            MessageBox.Show("output>>" + (String.IsNullOrEmpty(output) ? "(none)" : output));
            MessageBox.Show("error>>" + (String.IsNullOrEmpty(error) ? "(none)" : error));
            MessageBox.Show("ExitCode: " + ExitCode.ToString(), "ExecuteCommand");
            process.Close();
        }

        private void btReshape_Click(object sender, EventArgs e)
        {
            ExecuteBatFile1();
        }
        private void ExecuteBatFile1()
        {
            Process proc = null;
            try
            {
                pictureBox2.Image = null;

     
                string targetDir = string.Format(Constant.currentPath);   //this is where mybatch.bat lies
                
                proc = new Process();
                proc.StartInfo.WorkingDirectory = targetDir;
                proc.StartInfo.FileName = "make_reshape.bat";
                proc.StartInfo.Arguments=@""+Constant.pathImage+"";
                proc.StartInfo.CreateNoWindow = false;
              //  proc.StartInfo.WindowStyle = ProcessWindowStyle.Hidden;  //this is for hiding the cmd window...so execution will happen in back ground.
                proc.Start();
                proc.WaitForExit();
                //bmp = new Bitmap(@"" + Constant.currentPath + "\\bangdiem_reshape.png");
                //pictureBox2.Image = bmp;
                FileStream fileStream = new FileStream(@"" + Constant.currentPath + "\\bangdiem_reshape.png", FileMode.Open, FileAccess.Read);
                pictureBox2.Image = Image.FromStream(fileStream);
                fileStream.Close();
            }
            catch (Exception ex)
            {
                Console.WriteLine("Exception Occurred :{0},{1}", ex.Message, ex.StackTrace.ToString());
            }
        }
        public void ExecuteCommand1(string command)
        {
            int ExitCode;
            ProcessStartInfo ProcessInfo;
            Process process;

            ProcessInfo = new ProcessStartInfo(Application.StartupPath + "\\Python_Master\\make_reshape.bat", command);
            ProcessInfo.CreateNoWindow = true;
            ProcessInfo.UseShellExecute = false;
            ProcessInfo.WorkingDirectory = Application.StartupPath + "\\Python_Master";
            // *** Redirect the output ***
            ProcessInfo.RedirectStandardError = true;
            ProcessInfo.RedirectStandardOutput = true;

            process = Process.Start(ProcessInfo);
            process.WaitForExit();

            // *** Read the streams ***
            string output = process.StandardOutput.ReadToEnd();
            string error = process.StandardError.ReadToEnd();

            ExitCode = process.ExitCode;

            MessageBox.Show("output>>" + (String.IsNullOrEmpty(output) ? "(none)" : output));
            MessageBox.Show("error>>" + (String.IsNullOrEmpty(error) ? "(none)" : error));
            MessageBox.Show("ExitCode: " + ExitCode.ToString(), "ExecuteCommand");
            process.Close();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
                Constant.currentPath = System.IO.Directory.GetCurrentDirectory();
                Constant.currentPath = System.IO.Directory.GetParent(Constant.currentPath).FullName;
                Constant.currentPath = System.IO.Directory.GetParent(Constant.currentPath).FullName;
                Constant.currentPath += "\\Python_Master";
        }
    }
}
