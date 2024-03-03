package Java.reflection;

import java.lang.annotation.Annotation;
import java.lang.annotation.Retention;
import java.lang.annotation.RetentionPolicy;
import java.lang.annotation.Target;
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;

public class ReflectionTest
{
    public static void main(String argv[]) throws ClassNotFoundException, NoSuchMethodException, SecurityException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException
    {
        AService service = new AServiceImpl();

        service.execute();
        service.execute2();
        
        Class aClass = service.getClass();
        //Class bClass = Class.forName("java.reflection.ReflectionTest$AServiceImpl");
        Class<AServiceImpl> cClass = AServiceImpl.class;

        System.console().writer().println(aClass.getName());
        //System.console().writer().println(bClass.getName());
        System.console().writer().println(cClass.getName());

        Constructor constructor = aClass.getConstructor();
        Object object = constructor.newInstance();
        AService aService = (AService) object;

        aService.execute();
        aService.execute2();

        for (Field field : aClass.getDeclaredFields())
        {
            field.setAccessible(true);
            String fieldInfo = field.getType() + ", " + field.getName() + " = " + field.get(aService);
            System.out.println(fieldInfo);
        }

        // for (Method method : aClass.getMethods())
        // {
        //     System.out.println("Method Invoke Start");
        //     method.invoke(aService);
        //     System.out.println("Method Invoke End");
        // }

        for (Annotation annotation : aClass.getAnnotations())
        {
            System.out.println(annotation.toString());
        }
    }

    @AAnnotation("AServiceAnnoation")
    public static class AServiceImpl implements AService
    {
        private String name = "ASeriveName";

        @Override
        public String execute() {
            System.console().writer().println("AService Executed");
            return "A";
        }

        @Override
        public String execute2() {
            System.console().writer().println("AService Executed2");
            return "B";
        }

    }

    public interface AService
    {
        String execute();
        String execute2();
    }

    
    @Retention(RetentionPolicy.RUNTIME)
    public @interface AAnnotation{
        String value();
    }

}