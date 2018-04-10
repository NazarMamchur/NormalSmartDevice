package restPost;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpMethod;
import org.springframework.http.ResponseEntity;
import org.springframework.web.client.RestTemplate;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;

@SpringBootApplication
public class Application {

    private static final Logger log = LoggerFactory.getLogger(Application.class);

    public static void main(String args[]) {
        SpringApplication.run(Application.class);
    }

    @Bean
    public RestTemplate restTemplate(RestTemplateBuilder builder) {
        return builder.build();
    }

    @Bean
    public CommandLineRunner run(RestTemplate restTemplate) throws Exception {
        String directory = "D:\\IntelliJ IDEA 2017.2.5\\RestPOST\\src\\main\\resources\\";
        File file = new File(directory, "image.jpg");
        String base64String = encode(file);
        return args -> {
            HttpHeaders requestHeaders = new HttpHeaders();
            requestHeaders.add(HttpHeaders.CONTENT_TYPE, "application/x-www-form-urlencoded");
            ResponseEntity<String> response = restTemplate.exchange("http://localhost:9000/demo/isAllowed?base64String="
                    + base64String, HttpMethod.POST, null, String.class);
            log.info(response.toString());
            System.out.println("5-th char is - " + response.getBody());
        };
    }

    private String encode (File file) throws IOException {
        ByteArrayOutputStream byteArr = new ByteArrayOutputStream();
        BufferedImage image = ImageIO.read(file);

        ImageIO.write(image, "jpg", byteArr);
        byteArr.flush();

        String base64String = Base64.encode(byteArr.toByteArray());
        byteArr.close();
        return base64String;
    }
}
