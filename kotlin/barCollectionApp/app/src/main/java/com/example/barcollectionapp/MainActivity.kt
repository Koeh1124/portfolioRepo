package com.example.barcollectionapp

//import android.hardware.SensorEventListener
//https://www.techiedelight.com/write-json-to-a-file-in-kotlin/
import android.annotation.SuppressLint
import android.content.Context
import android.content.pm.PackageManager
import android.hardware.Sensor
import android.hardware.SensorEvent
import android.hardware.SensorEventListener
import android.hardware.SensorManager
import android.location.Location
import android.location.LocationListener
import android.location.LocationManager
import android.os.Build
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TableLayout
import android.widget.TableRow
import android.widget.TextView
import androidx.annotation.RequiresApi
import androidx.appcompat.app.AppCompatActivity
import androidx.core.app.ActivityCompat
import androidx.core.content.ContextCompat
import org.json.JSONException
import org.json.JSONObject
import java.io.File
import java.io.FileReader
import java.io.FileWriter
import java.text.SimpleDateFormat
import java.util.*

//allows us to request permissions and see the permissions we have

class MainActivity : AppCompatActivity(), SensorEventListener, LocationListener {

    //init sensors
    private lateinit var sensorManager: SensorManager
    private lateinit var locationManager: LocationManager
    private var pressure: Sensor? = null
    //private var temp: Sensor? =null
    //var to allow us to turn data collection on and off
    private var collectData = false
    private var pressureVal = 0.0
    private var long = 0.1
    private var lat = 0.1
    //${LocalDateTime.now().format(formatter)}
    private val locationPermissionCode = 2
    private val json = JSONObject()
    private val date = Date()
    @SuppressLint("SimpleDateFormat")
    private val formatFileName = SimpleDateFormat("yyyyMMdd")
    private var fileName = """/${formatFileName.format(date)}.json"""
    @SuppressLint("SimpleDateFormat")
    private val formatTS = SimpleDateFormat("HH:mm:ss")

    override fun onCreate(savedInstanceState: Bundle?) {
        readFile()
        getLocation()
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val startBtn = findViewById<Button>(R.id.button)
        findViewById<TextView>(R.id.testPrint)
        //defining the sensor
        sensorManager = getSystemService(SENSOR_SERVICE) as SensorManager
        pressure = sensorManager.getDefaultSensor(Sensor.TYPE_PRESSURE)
        //temp = sensorManager.getDefaultSensor(Sensor.TYPE_AMBIENT_TEMPERATURE);
        //on click listener to start the data collection
        startBtn.setOnClickListener {
            startCollection()
            Log.d("pressedButton?","btn pressed")
        }
    }

    private fun startCollection() {
        collectData = !collectData
        createFile()
        Log.d("collect Data CHanged",collectData.toString())
    }

    private fun createFile() {
        Log.d("file","trying to create")
        val lroot = (this.getExternalFilesDir(null))
        //var fileName = """${LocalDateTime.now().format(formatter)}.json""";
        //Datetime.now() is not included in sdk25
        Log.d("root",lroot.toString())
        Log.d("file",fileName)
        val file = File(getExternalFilesDir(null).toString()+fileName)
        if (file.delete()){
            Log.d("file","deleted")
        }
        if (file.createNewFile()){
            Log.d("file","created")
        }
        else{
            Log.d("file","already created")
            readFile()
        }
    }


    @RequiresApi(Build.VERSION_CODES.O)
    private fun addRow(bar: Double){
        val date = Date()
        readFile()
        val tableLayout = findViewById<TableLayout>(R.id.tableLayout)
        val tableRow = TableRow(this)
        val tsCol = TextView(this)
        Calendar.getInstance().time
        tsCol.text = formatTS.format(date)
        tableRow.addView(tsCol)
        val barCol = TextView(this)
        barCol.text = bar.toString()
        tableRow.addView(barCol)
        tableLayout.addView(tableRow)
        writeFile(formatTS.format(date),bar)
    }

    // On barometer change
    @RequiresApi(Build.VERSION_CODES.O)
    override fun onSensorChanged(event: SensorEvent) {
        if (event.sensor.type == Sensor.TYPE_PRESSURE){
            //Log.d("Pressure Val", event.values[0].toString())
            pressureVal = event.values[0].toDouble()
        }
        if (collectData) {
            addRow(pressureVal)
        }
    }

    //https://www.tutorialspoint.com/how-to-get-the-current-gps-location-programmatically-on-android-using-kotlin
    private fun getLocation() {
        locationManager = getSystemService(Context.LOCATION_SERVICE) as LocationManager
        //if we don't have permission we need to request it
        if ((ContextCompat.checkSelfPermission(this,android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED)) {
            ActivityCompat.requestPermissions(this, arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION), locationPermissionCode)
        }
        locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,0,5f,this)
    }
    override fun onLocationChanged(location: Location) {
        lat = location.latitude
        long = location.longitude
    }

    private fun writeFile(ts: String, bar: Double) {
        try{
        json.put(ts, """${bar},${long},${lat}""")
        } catch (e: JSONException){
            Log.d("Json:","made an oppsie")
        }
        try {
            FileWriter(getExternalFilesDir(null).toString()+fileName, false).use { it.write(json.toString()) }
            Log.d("file","write")
        } catch (e: Exception) {
            Log.d("file","write")
            e.printStackTrace()
        }
    }

    private fun readFile(){
        try {
            val testView = findViewById<TextView>(R.id.testPrint)
            val data = FileReader(getExternalFilesDir(null).toString()+fileName)
            testView.text = data.readText()
        } catch (e: Exception){

        }
    }

    override fun onAccuracyChanged(sensor: Sensor, acc: Int) {
        Log.d("Accuracy ","Changed")
    }
    //Taken from cp-max android file, makes stuff work for some reason. (I think it makes the sensor stop and stop)
    @SuppressWarnings("MissingPermission")
    override fun onResume() {
        // Register a listener for the sensor.
        super.onResume()
        sensorManager.registerListener(this, pressure, 10000000)
        //sensorManager.registerListener(this, temp, 10000000)
    }

    @SuppressWarnings("MissingPermission")
    override fun onPause() {
        // Be sure to unregister the sensor when the activity pauses.
        super.onPause()
        sensorManager.unregisterListener(this)
    }
}