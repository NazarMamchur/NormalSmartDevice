package postMapping;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.imageio.ImageIO;
import javax.script.*;
import java.awt.image.BufferedImage;
import java.io.*;

@Controller
@RequestMapping(path="/demo") // This means URL's start with /demo (after Application path)
public class MainController {

    String directory = "D:\\IntelliJ IDEA 2017.2.5\\RESTfulServer\\src\\main\\resources\\";

    @PostMapping(path="/isAllowed")
    public @ResponseBody String isAllowed (@RequestParam String base64String) throws IOException {
        base64String = correctString(base64String);
        toPhoto(base64String, "resultImage.jpg");

//        String result = null;
//        try {
//            result = pythonExecute("FaceRecognition.py");
//            System.out.println(result);
//        } catch (ScriptException e) {
//            e.printStackTrace();
//        }
//        return result;
        return String.valueOf(base64String.charAt(5));
    }

    private void toPhoto (String base64String, String fileName) throws IOException{
        byte[] resByteArray = Base64.decode(base64String);
        BufferedImage resultImage = ImageIO.read(new ByteArrayInputStream(resByteArray));
        ImageIO.write(resultImage, "jpg", new File(directory, fileName));
    }

    private String pythonExecute(String fileName) throws ScriptException, IOException {

        StringWriter writer = new StringWriter();
        ScriptContext context = new SimpleScriptContext();
        context.setWriter(writer);

        ScriptEngineManager manager = new ScriptEngineManager();
        ScriptEngine engine = manager.getEngineByName("python");
        FileReader reader = new FileReader(new File(directory, fileName));
        engine.eval("D:\\IntelliJ IDEA 2017.2.5\\RESTfulServer\\src\\main\\resources\\FaceRecognition.py", context);
        System.out.println(writer.toString());
        return writer.toString();
    }

    private String correctString(String base64String) {
        char [] string = base64String.toCharArray();
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < string.length; i++) {
            if (string[i] == ' ')
                string[i] = '+';
            result.append(string[i]);
        }
        return result.toString();
    }
}